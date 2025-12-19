# Implementation Plan - The "Ultimate" Upgrade

## Goal Description
Transform the portfolio manager into a full-featured crypto tracking suite. Key additions include detailed Profit/Loss analysis, Transaction History, Multi-currency support, Price Alerts, and a News Feed.

## Architecture & Database
- **Database**: SQLite with `portfolio`, `transactions`, and `alerts` tables.
- **Avg Price Logic**: Weighted average cost basis tracking for all trades.
- **Real-time**: Ajax polling for dashboard updates.

## Major Features
- **Trading**: Partial sell capability with balance validation.
- **Explorer**: Global market browsing with live charts.
- **Analytics**: Doughnut and Line charts for portfolio health.
- **Export**: CSV generation for financial reporting.
