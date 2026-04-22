CREATE TABLE trade_db.normalized_trades AS
SELECT
 trade_id,
 trader_id,
 symbol,
 quantity,
 price,
 side,
 CASE WHEN side='BUY' THEN -1 ELSE 1 END * quantity * price AS pnl,
 trade_date
FROM trade_db.raw_trades;
