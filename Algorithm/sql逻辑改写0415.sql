#改写sql逻辑:
######
#我们这里以fbicsi.lp_prft_poc3_oot_loanmob6_for_us为主表进行特征的衍生，该表主键
#包含card_no和date,最终衍生特征主键也基本遵循该流程 -> cust_ids, loan_date

#关联户头号:
DROP TABLE IF EXISTS usfinance.Features_MainTB_Meiyan;
CREATE TABLE usfinance.FinanceFeaturesMainTB_Meiyan AS 
SELECT * FROM 
(SELECT DISTINCT
    card_no AS cust_ids,
    date AS loan_date
    FROM fbicsi.lp_prft_poc3_oot_loanmob6_for_us) A
LEFT JOIN
(
SELECT DISTINCT
    id_card AS cust_ids,
    acct_no,
    member_id
    FROM finance.mls_member_info_all) B
ON A.cust_ids = B.cust_ids;

#关联金融app主表：
DROP TABLE IF EXISTS usfinance.JRAppFeatures_MainTB_Meiyan;
CREATE TABLE usfinance.FinanceFeaturesMainTB_Meiyan AS 
SELECT * FROM 
(
SELECT DISTINCT
       card_no AS cust_ids,
       date AS loan_date
       FROM fbicsi.Features_MainTB_Meiyan
) A
JOIN
(
SELECT 
    pv_id,
    acct_no,
    dev_id,
    user_bhvr_type,
    page_name,
    page_url,
    from_page_id,
    city,
    stat_date,
    page_nm,
    clct_ts,
    visit_drtn,
    from_page_name,
    from_page_url,
    spv_uv_flg,
    down_chnl_cd,
    app_type_cd,
    dev_mdl_cd,
    trmnl_type,
    new_visitor_flg,
    os_version_cd,
    page_in_time,
    page_out_time
    FROM FDM_SOR.T_FSA_BHVR_NEW_D
    WHERE stat_date <= "20200701") B
ON  A.acct_no = B.acct_no
WHERE 
    A.loan_date > B.page_out_time OR 
    A.loan_date > B.page_in_time OR 
    A.loan_date > B.clct_ts;

#关联易购app轨迹:
DROP TABLE IF EXISTS usfinance.YGAppFeatures_MainTB_Meiyan;
CREATE TABLE usfinance.YGAppFeatures_MainTB_Meiyan AS 
SELECT * FROM 
(SELECT coll_time,
       memb_id AS member_id,
       from_page_beg_time,
       page_nm,
       from_page_end_time,
       dev_trmnl_tp_cd,
       spv_uv_flg,
       shop_id,
       city_cd,
       dev_mdl_cd,
       pv_id,
       statis_date,
       from_page_url
       FROM brock_dwd.t_log_flx_web_page_view_d
WHERE statis_date >= "20200101" 
  AND from_page_url is not null 
  AND length(from_page_url) > 5 
  AND length(member_id) = 10) A
RIGHT JOIN
usfinance.FinanceFeaturesMainTB_Meiyan AS B
ON A.member_id = B.member_id
AND B.loan_date >= A.coll_time;

#关联oms交易信息：
DROP TABLE IF EXISTS usfinance.TransactionFeatures_MainTB_Meiyan;
CREATE TABLE usfinance.TransactionFeatures_MainTB_Meiyan AS 
SELECT * FROM 
((SELECT pay_tp_aray,
       vendor_cd,
       statis_date,
       b2c_ord_id,
       gds_cd,
       pay_amt,
       sal_qty,
       memb_card_id AS member_id,
       pay_time,
       statis_date,
       regexp_extract(pay_tp_aray, "pay_name\":(.*?),\"", 1) AS pay_name
FROM BROCK_DWD.T_ORD_RETAIL_GRP_ORD_DTL_D
WHERE statis_date >= "20200101" AND 
      pay_name NOT LIKE '%线下%' AND 
      (pay_name LIKE '%微信%' OR pay_name LIKE '%支付宝%') AND
      pay_time is not null AND
      vendor_cd LIKE '7% ') AS A
JOIN
(SELECT gds_cd,
       l4_gds_grp_desc AS catgroup_id,
       l3_gds_grp_desc
FROM 
       BROCK_DIM.T_PRD_GDS_INF_ED) AS B
ON A.gds_cd = B.gds_cd) AS C
JOIN usfinance.FinanceFeaturesMainTB_Meiyan AS D
ON C.member_id = D.member_id;

#理财特征
DROP TABLE IF EXISTS usfinance.licaiFeaturesBlock1_Meiyan;
CREATE TABLE usfinance.licaiFeaturesMainTB_Meiyan AS 
SELECT cust_ids,
       loan_date,
       COUNT(DISTINCT order_no) AS past_60d_fund_purchase_count,
       SUM(tot_amt) AS past_60d_fund_purchase_amt
FROM 
(finance.dpa_txn_fnd_prch_order A 
RIGHT JOIN
usfinance.Features_MainTB_Meiyan B 
ON A.acct_no = B.acct_no
WHERE A.pay_time <= B.loan_date AND DATEDIFF(loan_date, pay_time) <= 60) A
GROUP BY cust_ids, loan_date;


#衍生易购app特征指标:
DROP TABLE IF EXISTS usfinance.YGAppBlock1_Meiyan;
CREATE TABLE usfinance.YGAppBlock1_Meiyan AS 
SELECT cust_ids,
       loan_date,
       COUNT(DISTINCT (
       	CASE WHEN 
       	pv_id is not null AND (DATEDIFF(loan_date, page_out_date) <= 180 OR DATEDIFF(loan_date, page_in_date) <= 180 OR DATEDIFF(loan_date, coll_date) <= 180)
       	THEN pv_id END
       	)) AS YGpast_180d_vst_count,
       SUM(CASE WHEN 
       	pv_id is not null AND (DATEDIFF(loan_date, page_out_date) <= 180 OR DATEDIFF(loan_date, page_in_date) <= 180 OR DATEDIFF(loan_date, coll_date) <= 180)
       	THEN visit_drtn_minute ELSE 0 END) AS YGpast_180d_vst_length,
       SUM(CASE WHEN
       	pv_id is not null AND page_nm LIKE '%购物车%' AND (DATEDIFF(loan_date, page_out_date) <= 180 OR DATEDIFF(loan_date, page_in_date) <= 180 OR DATEDIFF(loan_date, coll_date) <= 180)
       	THEN visit_drtn_minute ELSE 0 END) AS YGpast_180d_shoppingcard_vst_length,
       COUNT(DISTINCT(
       	CASE WHEN DATEDIFF(loan_date, page_out_date) <= 180 OR DATEDIFF(loan_date, page_in_date) <= 180 OR DATEDIFF(loan_date, coll_date) <= 180
       	THEN dev_mdl_cd END
       	)) AS YGpast_180d_dev_mdl_cd_count,
       COUNT(DISTINCT(
       	CASE WHEN pv_id is not null AND page_name LIKE '%购物车%' AND (DATEDIFF(loan_date, page_out_date) <= 180 OR DATEDIFF(loan_date, page_in_date) <= 180 OR DATEDIFF(loan_date, coll_date) <= 180)
       	THEN pv_id END
       	)) AS YGpast_180d_shoppingcard_vst_count,
       COUNT(DISTINCT(
       	CASE WHEN pv_id is not null AND (DATEDIFF(loan_date, page_out_date) <= 360 OR DATEDIFF(loan_date, page_in_date) <= 360 OR DATEDIFF(loan_date, coll_date) <= 360)
       	THEN pv_id END
       	)) AS YGpast_360d_vst_count,
       SUM(CASE WHEN 
       	pv_id is not null AND (DATEDIFF(loan_date, page_out_date) <= 360 OR DATEDIFF(loan_date, page_in_date) <= 360 OR DATEDIFF(loan_date, coll_date) <= 360)
       	THEN visit_drtn_minute ELSE 0 END) AS YGpast_360d_vst_length,
       COUNT(DISTINCT(
       	CASE WHEN (DATEDIFF(loan_date, page_out_date) <= 360 OR DATEDIFF(loan_date, page_in_date) <= 360 OR DATEDIFF(loan_date, coll_date) <= 360)
       	THEN city_cd END
       	)) AS YGpast_360d_pageview_city_count,
       SUM(CASE WHEN 
       	pv_id is not null AND page_nm LIKE '%购物车%' AND (DATEDIFF(loan_date, page_out_date) <= 90 OR DATEDIFF(loan_date, page_in_date) <= 90 OR DATEDIFF(loan_date, coll_date) <= 90)
       	THEN visit_drtn_minute ELSE 0 END) AS YGpast_90d_shoppingcard_vst_length
FROM 
(SELECT cust_ids,
       pv_id,
       page_nm,
       dev_mdl_cd,
       city_cd,
       loan_date,
       substring(coll_date, 1, 10) AS coll_date,
       substring(from_page_beg_time, 1, 10) AS page_in_date,
       substring(from_page_end_time, 1, 10) AS page_out_date,
       (unix_timestamp(from_page_end_time) - unix_timestamp(from_page_beg_time))/(60.0) AS visit_drtn_minute
FROM usfinance.YGAppFeatures_MainTB_Meiyan
WHERE page_in_date = page_out_date OR (unix_timestamp(from_page_end_time) - unix_timestamp(from_page_beg_time)) <= 86400) AS A1
GROUP BY cust_ids, loan_date;

SELECT cust_ids,
       loan_date,
       max(pv_count) AS YGmax_daily_visit_count_360days,
       max(visit_dif) AS YGmax_daily_visit_dur_360days
FROM 
(SELECT cust_ids,
       loan_date,
       coll_date,
       COUNT(DISTINCT (
       	CASE WHEN pv_id is not null THEN pv_id END
       	)) AS pv_count,
       SUM(CASE WHEN pv_id is not null THEN visit_drtn_minute ELSE 0 END) AS visit_dif
FROM 
(SELECT cust_ids,
       pv_id,
       page_nm,
       dev_mdl_cd,
       city_cd,
       loan_date,
       substring(coll_date, 1, 10) AS coll_date,
       substring(from_page_beg_time, 1, 10) AS page_in_date,
       substring(from_page_end_time, 1, 10) AS page_out_date,
       (unix_timestamp(from_page_end_time) - unix_timestamp(from_page_beg_time))/(60.0) AS visit_drtn_minute
FROM usfinance.YGAppFeatures_MainTB_Meiyan
WHERE page_in_date = page_out_date OR (unix_timestamp(from_page_end_time) - unix_timestamp(from_page_beg_time)) <= 86400) AS A1
GROUP BY cust_ids, loan_date, coll_date) AS A2
GROUP BY cust_ids, loan_date;

#交易/支付相关指标衍生:
DROP TABLE IF EXISTS usfinance.TransactionFeaturesBlock1_Meiyan;
CREATE TABLE usfinance.TransactionFeaturesBlock1_Meiyan AS 
SELECT cust_ids,
       loan_date,
       COUNT(DISTINCT(
       	CASE WHEN DATEDIFF(loan_date, pay_time) <= 30 THEN b2c_ord_id END
       	)) AS id_card_wxzfb_whole_order_past_30d,
       COUNT(DISTINCT(
       	CASE WHEN (pay_hour <= 7 OR pay_hour >= 21) AND DATEDIFF(loan_date, pay_time) <= 30 THEN b2c_ord_id END
       	)) AS id_card_wxzfb_latenight_whole_order_count_past_30d,
       COUNT(DISTINCT(
       	CASE WHEN DATEDIFF(loan_date, pay_time) <= 90 THEN b2c_ord_id END
       	)) AS id_card_wxzfb_whole_order_past_90d,
       COUNT(DISTINCT(
       	CASE WHEN DATEDIFF(loan_date, pay_time) <= 90 AND (pay_hour <= 7 OR pay_hour >= 21) THEN b2c_ord_id END
       	)) AS id_card_wxzfb_latenight_whole_order_count_past_90d
FROM
(SELECT DISTINCT
       pay_name,
       cust_ids,
       loan_date,
       b2c_ord_id,
       pay_amt,
       sal_qty,
       pay_time,
       CASE(substring(pay_time, 12, 1) AS int) AS pay_hour
 FROM usfinance.TransactionFeatures_MainTB_Meiyan
WHERE 
    pay_name NOT LIKE '%线下%' AND 
    (pay_name LIKE '%微信%' OR pay_name LIKE '%支付宝%') AND
    loan_date >= pay_time) AS A1
GROUP BY cust_ids, loan_date;

DROP TABLE IF EXISTS usfinance.TransactionFeaturesBlock2_Meiyan;
CREATE TABLE usfinance.TransactionFeaturesBlock2_Meiyan AS 
SELECT cust_ids, 
       loan_date,
       max(vendor_order_count)
FROM 
(SELECT vendor_cd,
       cust_ids,
       loan_date,
       COUNT(DISTINCT b2c_ord_id) AS vendor_order_count
FROM 
(SELECT DISTINCT
       pay_name,
       cust_ids,
       loan_date,
       b2c_ord_id,
       pay_amt,
       sal_qty,
       pay_time,
       CASE(substring(pay_time, 12, 1) AS int) AS pay_hour
 FROM usfinance.TransactionFeatures_MainTB_Meiyan
WHERE 
    pay_name NOT LIKE '%线下%' AND 
    (pay_name LIKE '%微信%' OR pay_name LIKE '%支付宝%') AND
    loan_date >= pay_time AND
    DATEDIFF(day, pay_time, loan_date) <= 180) AS A1
GROUP BY vendor_cd, cust_ids, loan_date) AS A2
GROUP BY cust_ids, loan_date;


#金融app轨迹特征:
DROP TABLE IF EXISTS usfinance.JRAppFeaturesBlock1_Meiyan;
CREATE TABLE usfinance.JRAppFeaturesBlock1_Meiyan AS 
SELECT cust_ids,
       loan_date,
       AVG(CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 7 OR DATEDIFF(loan_date, page_out_time) <= 7 OR DATEDIFF(loan_date, clct_ts) <= 7)
       	AND spv_uv_flg != 1 AND page_name LIKE '%拒绝%' AND visit_dif > 0 
       	THEN visit_dif END ) AS visit_7days_length_rejection,     
       AVG(CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 15 OR DATEDIFF(loan_date, page_out_time) <= 15 OR DATEDIFF(loan_date, clct_ts) <= 15)
       	AND spv_uv_flg != 1 AND (page_name LIKE '%任性贷%' OR page_name LIKE '%任性付%' OR page_name LIKE '%免息商城%') AND visit_dif > 0
       	THEN visit_dif ELSE 0 END) AS visit_15days_avg_length_rxdrxf,
       AVG(CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 60 OR DATEDIFF(loan_date, page_out_time) <= 60 OR DATEDIFF(loan_date, clct_ts) <= 60)
       	AND spv_uv_flg != 1 AND (page_name LIKE '%任性贷%' OR page_name LIKE '%任性付%' OR page_name LIKE '%免息商城%') AND visit_dif > 0
       	THEN visit_dif ELSE 0 END) AS visit_60days_avg_length_rxdrxf,    
       AVG(CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 90 OR DATEDIFF(loan_date, page_out_time) <= 90 OR DATEDIFF(loan_date, clct_ts) <= 90)        AND spv_uv_flg != 1 AND (page_name LIKE '%任性贷%' OR page_name LIKE '%任性付%' OR page_name LIKE '%免息商城%') AND visit_dif > 0
        THEN visit_dif ELSE 0 END) AS visit_90days_avg_length_rxdrxf,  
       SUM(CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 180 OR DATEDIFF(loan_date, page_out_time) <= 180 OR DATEDIFF(loan_date, clct_ts) <= 180)
       	AND spv_uv_flg != 1 AND (page_name LIKE '%任性贷%' OR page_name LIKE '%任性付%' OR page_name LIKE '%免息商城%') AND visit_dif > 0
       	THEN visit_dif ELSE 0 END) AS visit_180days_length_rxdrxf,       
       AVG(CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 30 OR DATEDIFF(loan_date, page_out_time) <= 30 OR DATEDIFF(loan_date, clct_ts) <= 30)
       	AND spv_uv_flg != 1 AND page_name LIKE '%拒绝%' AND visit_dif > 0
       	THEN visit_dif ELSE 0 END) AS visit_30days_avg_length_rejection,
       AVG(CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 30 OR DATEDIFF(loan_date, page_out_time) <= 30 OR DATEDIFF(loan_date, clct_ts) <= 30)
       	AND spv_uv_flg != 1 AND page_name LIKE '%账单%' AND visit_dif > 0
       	THEN visit_dif ELSE 0 END) AS visit_30days_avg_length_bill,
       AVG(CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 90 OR DATEDIFF(loan_date, page_out_time) <= 90 OR DATEDIFF(loan_date, clct_ts) <= 90)
       	AND spv_uv_flg != 1 AND (page_name LIKE '%理财%' OR page_name LIKE '%基金%' OR page_name LIKE '%零钱宝%' OR page_name LIKE '%保险%') AND visit_dif > 0
       	THEN visit_dif ELSE 0 END) AS visit_90days_avg_length_financing,
       AVG(CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 90 OR DATEDIFF(loan_date, page_out_time) <= 90 OR DATEDIFF(loan_date, clct_ts) <= 90)
       	AND spv_uv_flg != 1 AND page_name LIKE '%拒绝%' AND visit_dif > 0
       	THEN visit_dif ELSE 0 END) AS visit_90days_avg_length_rejection,
       SUM(CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 60 OR DATEDIFF(loan_date, page_out_time) <= 60 OR DATEDIFF(loan_date, clct_ts) <= 60)
        AND spv_uv_flg != 1 AND (page_name LIKE '%任性贷%' OR page_name LIKE '%任性付%' OR page_name LIKE '%免息商城%') AND visit_dif > 0
        THEN visit_dif ELSE 0 END) AS visit_60days_length_rxdrxf,
       SUM(CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 90 OR DATEDIFF(loan_date, page_out_time) <= 90 OR DATEDIFF(loan_date, clct_ts) <= 90)
       	AND spv_uv_flg != 1 AND (page_name LIKE '%任性贷%' OR page_name LIKE '%任性付%' OR page_name LIKE '%免息商城%') AND visit_dif > 0
       	THEN visit_dif ELSE 0 END) AS visit_90days_length_rxdrxf,
       SUM(CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 90 OR DATEDIFF(loan_date, page_out_time) <= 90 OR DATEDIFF(loan_date, clct_ts) <= 90)
        AND spv_uv_flg != 1 AND page_name LIKE '%拒绝%' AND visit_dif > 0
        THEN visit_dif ELSE 0 END) AS visit_90days_length_rejection,      
       SUM(CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 60 OR DATEDIFF(loan_date, page_out_time) <= 60 OR DATEDIFF(loan_date, clct_ts) <= 60)
        AND spv_uv_flg != 1 AND page_name LIKE '%拒绝%' AND visit_dif > 0
        THEN visit_dif ELSE 0 END) AS visit_60days_length_rejection,   
       SUM(CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 90 OR DATEDIFF(loan_date, page_out_time) <= 90 OR DATEDIFF(loan_date, clct_ts) <= 90)
       	AND spv_uv_flg != 1 AND (page_name LIKE '%理财%' OR page_name LIKE '%基金%' OR page_name LIKE '%零钱宝%' OR page_name LIKE '%保险%') AND visit_dif > 0
       	THEN visit_dif ELSE 0 END) AS visit_360days_length_financing,
       AVG(CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 360 OR DATEDIFF(loan_date, page_out_time) <= 360 OR DATEDIFF(loan_date, clct_ts) <= 360)
       	AND spv_uv_flg != 1 AND page_name LIKE '%拒绝%' AND visit_dif > 0
       	THEN visit_dif ELSE 0 END) AS visit_360days_avg_length_rejection,
       AVG(CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 60 OR DATEDIFF(loan_date, page_out_time) <= 60 OR DATEDIFF(loan_date, clct_ts) <= 60)
       	AND spv_uv_flg != 1 AND page_name LIKE '%拒绝%' AND visit_dif > 0
       	THEN visit_dif ELSE 0 END) AS visit_60days_avg_length_rejection,
       AVG(CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 180 OR DATEDIFF(loan_date, page_out_time) <= 180 OR DATEDIFF(loan_date, clct_ts) <= 180)
        AND spv_uv_flg != 1 AND page_name LIKE '%拒绝%' AND visit_dif > 0
        THEN visit_dif ELSE 0 END) AS visit_180days_avg_length_rejection,       
       AVG(CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 60 OR DATEDIFF(loan_date, page_out_time) <= 60 OR DATEDIFF(loan_date, clct_ts) <= 60)
        AND spv_uv_flg != 1 AND (page_name LIKE '%理财%' OR page_name LIKE '%基金%' OR page_name LIKE '%零钱宝%' OR page_name LIKE '%保险%') AND visit_dif > 0
        THEN visit_dif ELSE 0 END) AS visit_60days_avg_length_financing,
       SUM(CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 60 OR DATEDIFF(loan_date, page_out_time) <= 60 OR DATEDIFF(loan_date, clct_ts) <= 60)
       	AND spv_uv_flg != 1 AND (page_name LIKE '%理财%' OR page_name LIKE '%基金%' OR page_name LIKE '%零钱宝%' OR page_name LIKE '%保险%') AND visit_dif > 0
       	THEN visit_dif ELSE 0 END) AS visit_60days_length_financing
FROM
(SELECT page_in_time,
       page_out_time,
       cust_ids,
       loan_date,
       page_name,
       pv_id,
       dev_mdl_cd,
       spv_uv_flg,
       clct_ts,
       ((unix_timestamp(page_out_time) - unix_timestamp(page_in_time))/(60.0)) AS visit_dif
FROM usfinance.JRAppFeatures_MainTB_Meiyan
WHERE substring(page_in_time, 1, 10) = substring(page_out_time, 1, 10) OR (unix_timestamp(page_out_time) - unix_timestamp(page_in_time)) <= 86400
) A1
GROUP BY cust_ids, loan_date;


DROP TABLE IF EXISTS usfinance.JRAppFeaturesBlock2_Meiyan;
CREATE TABLE usfinance.JRAppFeaturesBlock2_Meiyan AS 
SELECT cust_ids,
       loan_date,
       COUNT(DISTINCT(
       	CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 30 OR DATEDIFF(loan_date, page_out_time) <= 30 OR DATEDIFF(loan_date, clct_ts) <= 30)
       	AND spv_uv_flg != 1 AND pv_id is not null and page_name LIKE '%账单%'
       	THEN pv_id END
       	)) AS visit_30days_times_bill,
       COUNT(DISTINCT(
       	CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 60 OR DATEDIFF(loan_date, page_out_time) <= 60 OR DATEDIFF(loan_date, clct_ts) <= 60)
       	AND spv_uv_flg != 1 AND pv_id is not null and (page_name LIKE '%任性贷%' OR page_name LIKE '%任性付%' OR page_name LIKE '%免息商城%')
       	THEN pv_id END
       	)) AS visit_60days_times_rxdrxf,
       COUNT(DISTINCT(
       	CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 90 OR DATEDIFF(loan_date, page_out_time) <= 90 OR DATEDIFF(loan_date, clct_ts) <= 90)
       	AND spv_uv_flg != 1 AND pv_id is not null and (page_name LIKE '%任性贷%' OR page_name LIKE '%任性付%' OR page_name LIKE '%免息商城%')
       	THEN pv_id END
       	)) AS visit_90days_times_rxdrxf,
       COUNT(DISTINCT(
       	CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 180 OR DATEDIFF(loan_date, page_out_time) <= 180 OR DATEDIFF(loan_date, clct_ts) <= 180)
       	AND spv_uv_flg != 1 AND pv_id is not null and (page_name LIKE '%任性贷%' OR page_name LIKE '%任性付%' OR page_name LIKE '%免息商城%')
       	THEN pv_id END
       	)) AS visit_180days_times_rxdrxf,
       COUNT(DISTINCT(
       	CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 360 OR DATEDIFF(loan_date, page_out_time) <= 360 OR DATEDIFF(loan_date, clct_ts) <= 360)
       	AND spv_uv_flg != 1 AND pv_id is not null and (page_name LIKE '%理财%' OR page_name LIKE '%基金%' OR page_name LIKE '%零钱宝%' OR page_name LIKE '%保险%')
       	THEN pv_id END
       	)) AS visit_360days_times_financing,
        COUNT(DISTINCT(
       	CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 180 OR DATEDIFF(loan_date, page_out_time) <= 180 OR DATEDIFF(loan_date, clct_ts) <= 180)
       	AND spv_uv_flg != 1 AND pv_id is not null and (page_name LIKE '%理财%' OR page_name LIKE '%基金%' OR page_name LIKE '%零钱宝%' OR page_name LIKE '%保险%')
       	THEN clct_date END
       	)) AS visit_180days_days_financing, 
       	COUNT(DISTINCT(
       	CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 90 OR DATEDIFF(loan_date, page_out_time) <= 90 OR DATEDIFF(loan_date, clct_ts) <= 90)
       	AND spv_uv_flg != 1 AND pv_id is not null AND page_name LIKE '%拒绝%'
       	THEN pv_id END
       		)) AS visit_90days_times_rejection,
       	COUNT(DISTINCT (
       	CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 90 OR DATEDIFF(loan_date, page_out_time) <= 90 OR DATEDIFF(loan_date, clct_ts) <= 90)
       	AND spv_uv_flg != 1 AND pv_id is not null 
       	THEN city END
       		)) AS visit_90days_cnt_city,
       	AVG(CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 30 OR DATEDIFF(loan_date, page_out_time) <= 30 OR DATEDIFF(loan_date, clct_ts) <= 30)
       	AND spv_uv_flg != 1 AND visit_dif > 0.0 and (page_name LIKE '%理财%' OR page_name LIKE '%基金%' OR page_name LIKE '%零钱宝%' OR page_name LIKE '%保险%')
       	THEN visit_dif) AS visit_30days_length_financing,
       	COUNT(DISTICNT(
       	CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 360 OR DATEDIFF(loan_date, page_out_time) <= 360 OR DATEDIFF(loan_date, clct_ts) <= 360)
       	AND spv_uv_flg != 1 AND pv_id is not null
       	THEN pv_id END
       		)) AS visit_360days_times,
       	COUNT(DISTICNT(
       	CASE WHEN (DATEDIFF(loan_date, page_in_time) <= 60 OR DATEDIFF(loan_date, page_out_time) <= 60 OR DATEDIFF(loan_date, clct_ts) <= 60)
       	AND spv_uv_flg != 1 AND pv_id is not null
       	THEN pv_id END
       		)) AS visit_60days_times
FROM
(SELECT page_in_time,
       page_out_time,
       cust_ids,
       loan_date,
       page_name,
       pv_id,
       dev_mdl_cd,
       spv_uv_flg,
       clct_ts,
       ((unix_timestamp(page_out_time) - unix_timestamp(page_in_time))/(60.0)) AS visit_dif
FROM usfinance.JRAppFeatures_MainTB_Meiyan
WHERE substring(page_in_time, 1, 10) = substring(page_out_time, 1, 10) OR (unix_timestamp(page_out_time) - unix_timestamp(page_in_time)) <= 86400
) A1
GROUP BY cust_ids, loan_date;

DROP TABLE IF EXISTS usfinance.JRAppFeaturesBlock3_Meiyan;
CREATE TABLE usfinance.JRAppFeaturesBlock3_Meiyan AS 
SELECT cust_ids,
       loan_date,
       max(visit_dif) AS max_daily_visit_dur_30days
FROM
(SELECT cust_ids,
       loan_date,
       clct_date,
       SUM(CASE WHEN spv_uv_flg != 1 THEN visit_dif END) AS visit_dif
FROM
(SELECT page_in_time,
       page_out_time,
       cust_ids,
       loan_date,
       page_name,
       pv_id,
       dev_mdl_cd,
       spv_uv_flg,
       clct_ts,
       ((unix_timestamp(page_out_time) - unix_timestamp(page_in_time))/(60.0)) AS visit_dif
FROM usfinance.JRAppFeatures_MainTB_Meiyan
WHERE DATEDIFF(loan_date, page_out_time) <= 30
AND   DATEDIFF(loan_date, page_in_time) <= 30
AND   DATEDIFF(loan_date, clct_ts) <= 30
AND (substring(page_in_time, 1, 10) = substring(page_out_time, 1, 10) OR (unix_timestamp(page_out_time) - unix_timestamp(page_in_time)) <= 86400)) A1
GROUP BY cust_ids, loan_date, clct_date) A2
GROUP BY cust_ids, loan_date;

DROP TABLE IF EXISTS usfinance.JRAppFeaturesBlock4_Meiyan;
CREATE TABLE usfinance.JRAppFeaturesBlock4_Meiyan AS 
SELECT cust_ids,
       loan_date,
       max(pv_count) AS max_daily_visit_count_90days
FROM 
(SELECT cust_ids, 
       loan_date,
       clct_date,
       COUNT(DISTINCT(CASE WHEN 
       	spv_uv_flg != 1 AND pv_id is not null THEN pv_id END)) AS pv_count
FROM 
(SELECT page_in_time,
       page_out_time,
       cust_ids,
       loan_date,
       page_name,
       pv_id,
       dev_mdl_cd,
       spv_uv_flg,
       clct_ts,
       ((unix_timestamp(page_out_time) - unix_timestamp(page_in_time))/(60.0)) AS visit_dif
FROM usfinance.JRAppFeatures_MainTB_Meiyan
WHERE DATEDIFF(loan_date, page_out_time) <= 30
AND   DATEDIFF(loan_date, page_in_time) <= 30
AND   DATEDIFF(loan_date, clct_ts) <= 30
AND (substring(page_in_time, 1, 10) = substring(page_out_time, 1, 10) OR (unix_timestamp(page_out_time) - unix_timestamp(page_in_time)) <= 86400)) A1
GROUP BY cust_ids, loan_date, clct_date) A2
GROUP BY cust_ids, loan_date;


DROP TABLE IF EXISTS usfinance.JRAppFeaturesBlock5_Meiyan;
CREATE TABLE usfinance.JRAppFeaturesBlock5_Meiyan AS 
SELECT cust_ids,
       loan_date,
       max(pv_count) AS max_daily_visit_count_360days
FROM 
(SELECT cust_ids, 
       loan_date,
       clct_date,
       COUNT(DISTINCT(CASE WHEN 
       	spv_uv_flg != 1 AND pv_id is not null THEN pv_id END)) AS pv_count
FROM 
(SELECT page_in_time,
       page_out_time,
       cust_ids,
       loan_date,
       page_name,
       pv_id,
       dev_mdl_cd,
       spv_uv_flg,
       clct_ts,
       ((unix_timestamp(page_out_time) - unix_timestamp(page_in_time))/(60.0)) AS visit_dif
FROM usfinance.JRAppFeatures_MainTB_Meiyan
WHERE DATEDIFF(loan_date, page_out_time) <= 360
AND   DATEDIFF(loan_date, page_in_time) <= 360
AND   DATEDIFF(loan_date, clct_ts) <= 360
AND (substring(page_in_time, 1, 10) = substring(page_out_time, 1, 10) OR (unix_timestamp(page_out_time) - unix_timestamp(page_in_time)) <= 86400)) A1
GROUP BY cust_ids, loan_date, clct_date) A2
GROUP BY cust_ids, loan_date;



DROP TABLE IF EXISTS usfinance.JRAppFeaturesBlock6_Meiyan;
CREATE TABLE usfinance.JRAppFeaturesBlock6_Meiyan AS 
SELECT cust_ids,
       loan_date,
       (CASE WHEN earlist_clct_time >= "2015" 
       THEN DATEDIFF(day, earlist_clct_time, loan_date)
       ELSE null END) AS earlist_page_clct_time_before_loan
FROM
(SELECT cust_id,
       loan_date,
       min(clct_ts) AS earlist_clct_time
FROM
(SELECT page_in_time,
       page_out_time,
       cust_ids,
       loan_date,
       page_name,
       pv_id,
       dev_mdl_cd,
       spv_uv_flg,
       clct_ts,
       ((unix_timestamp(page_out_time) - unix_timestamp(page_in_time))/(60.0)) AS visit_dif
FROM usfinance.JRAppFeatures_MainTB_Meiyan 
WHERE (substring(page_in_time, 1, 10) = substring(page_out_time, 1, 10) OR (unix_timestamp(page_out_time) - unix_timestamp(page_in_time)) <= 86400)) A1
GROUP BY cust_ids, loan_date) AS A2;


