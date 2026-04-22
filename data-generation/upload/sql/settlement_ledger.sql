CREATE TABLE trade_db.settlement_ledger AS
SELECT
 symbol,
 SUM(pnl) AS total_pnl,
 COUNT(*) AS total_trades,
 current_date AS settlement_date
FROM trade_db.normalized_trades
GROUP BY symbol;
