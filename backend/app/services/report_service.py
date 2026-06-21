from pathlib import Path

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from openpyxl import Workbook

from app.services.analytics_engine import (
    AnalyticsEngine
)

from app.services.intelligence_engine import (
    IntelligenceEngine
)

from app.services.recommendation_engine import (
    RecommendationEngine
)

from app.repositories.portfolio_repository import (
    PortfolioRepository
)


class ReportService:

    @staticmethod
    def generate_portfolio_report(
        portfolio_id: str
    ):

        analytics = (
            AnalyticsEngine
            .get_portfolio_summary(
                portfolio_id
            )
        )

        intelligence = (
            IntelligenceEngine
            .get_portfolio_intelligence(
                portfolio_id
            )
        )

        recommendations = (
            RecommendationEngine
            .get_recommendations(
                portfolio_id
            )
        )

        return {

            "portfolio_id":
                portfolio_id,

            "generated_by":
                "XSAP Reporting Engine",

            "analytics":
                analytics,

            "intelligence":
                intelligence,

            "recommendations":
                recommendations
        }

    @staticmethod
    def generate_investor_statement(
        investor_id: str
    ):

        portfolios = (
            PortfolioRepository
            .get_portfolios_by_investor(
                investor_id
            )
        )

        total_market_value = 0
        total_cost_basis = 0
        total_profit_loss = 0

        portfolio_summaries = []

        for portfolio in portfolios:

            portfolio_id = portfolio.get(
                "portfolio_id"
            )

            analytics = (
                AnalyticsEngine
                .get_portfolio_summary(
                    portfolio_id
                )
            )

            market_value = analytics.get(
                "total_market_value",
                0
            )

            cost_basis = analytics.get(
                "total_cost_basis",
                0
            )

            profit_loss = analytics.get(
                "total_profit_loss",
                0
            )

            total_market_value += (
                market_value
            )

            total_cost_basis += (
                cost_basis
            )

            total_profit_loss += (
                profit_loss
            )

            portfolio_summaries.append(
                {
                    "portfolio_id":
                        portfolio_id,

                    "market_value":
                        round(
                            market_value,
                            2
                        ),

                    "profit_loss":
                        round(
                            profit_loss,
                            2
                        )
                }
            )

        roi = 0

        if total_cost_basis > 0:

            roi = round(
                (
                    total_profit_loss
                    / total_cost_basis
                ) * 100,
                2
            )

        return {

            "investor_id":
                investor_id,

            "total_portfolios":
                len(portfolios),

            "total_cost_basis":
                round(
                    total_cost_basis,
                    2
                ),

            "total_market_value":
                round(
                    total_market_value,
                    2
                ),

            "total_profit_loss":
                round(
                    total_profit_loss,
                    2
                ),

            "total_roi_percent":
                roi,

            "portfolios":
                portfolio_summaries
        }

    @staticmethod
    def generate_portfolio_pdf(
        portfolio_id: str
    ):

        report = (
            ReportService
            .generate_portfolio_report(
                portfolio_id
            )
        )

        output_dir = Path(
            "exports/pdf"
        )

        output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        file_path = (
            output_dir /
            f"{portfolio_id}_report.pdf"
        )

        document = (
            SimpleDocTemplate(
                str(file_path)
            )
        )

        styles = (
            getSampleStyleSheet()
        )

        content = []

        content.append(
            Paragraph(
                "Xeonsys Stock Analytics Platform",
                styles["Title"]
            )
        )

        content.append(
            Spacer(1, 12)
        )

        content.append(
            Paragraph(
                f"Portfolio Report: {portfolio_id}",
                styles["Heading2"]
            )
        )

        content.append(
            Spacer(1, 12)
        )

        analytics = report[
            "analytics"
        ]

        content.append(
            Paragraph(
                "Portfolio Analytics",
                styles["Heading3"]
            )
        )

        content.append(
            Paragraph(
                f"Total Cost Basis: GHS {analytics.get('total_cost_basis', 0)}",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Total Market Value: GHS {analytics.get('total_market_value', 0)}",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Total Profit/Loss: GHS {analytics.get('total_profit_loss', 0)}",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Portfolio ROI: {analytics.get('portfolio_roi_percent', 0)}%",
                styles["Normal"]
            )
        )

        content.append(
            Spacer(1, 12)
        )

        content.append(
            Paragraph(
                "Recommendations",
                styles["Heading3"]
            )
        )

        recommendations = report.get(
            "recommendations",
            []
        )

        for recommendation in recommendations:

            content.append(
                Paragraph(
                    f"• {recommendation}",
                    styles["Normal"]
                )
            )

        document.build(
            content
        )

        return {

            "message":
                "PDF report generated successfully",

            "file":
                str(file_path)
        }

    @staticmethod
    def generate_portfolio_excel(
        portfolio_id: str
    ):

        report = (
            ReportService
            .generate_portfolio_report(
                portfolio_id
            )
        )

        output_dir = Path(
            "exports/excel"
        )

        output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        file_path = (
            output_dir /
            f"{portfolio_id}_report.xlsx"
        )

        workbook = Workbook()

        worksheet = workbook.active

        worksheet.title = (
            "Portfolio Report"
        )

        analytics = report[
            "analytics"
        ]

        worksheet.append(
            [
                "Portfolio ID",
                portfolio_id
            ]
        )

        worksheet.append([])

        worksheet.append(
            [
                "Metric",
                "Value"
            ]
        )

        worksheet.append(
            [
                "Total Cost Basis",
                analytics.get(
                    "total_cost_basis",
                    0
                )
            ]
        )

        worksheet.append(
            [
                "Total Market Value",
                analytics.get(
                    "total_market_value",
                    0
                )
            ]
        )

        worksheet.append(
            [
                "Total Profit Loss",
                analytics.get(
                    "total_profit_loss",
                    0
                )
            ]
        )

        worksheet.append(
            [
                "Portfolio ROI %",
                analytics.get(
                    "portfolio_roi_percent",
                    0
                )
            ]
        )

        worksheet.append([])

        worksheet.append(
            [
                "Recommendations"
            ]
        )

        recommendations = report.get(
            "recommendations",
            []
        )

        for recommendation in recommendations:

            worksheet.append(
                [
                    recommendation
                ]
            )

        workbook.save(
            str(file_path)
        )

        return {

            "message":
                "Excel report generated successfully",

            "file":
                str(file_path)
        }