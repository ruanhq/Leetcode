#sql改写 
DROP TABLE IF EXISTS usfinance.FinanceTrajectoryFeatureMainTB_Credit;
CREATE TABLE usfinance.FinanceTrajectoryFeatureMainTB_Credit AS 
SELECT * FROM 
(
SELECT DISTINCT
       loan_no,
       cust_ids,
       is_overdue_flag,
       loan_date,
       acct_no
       FROM usfinance.userWholeBcard_RHQ
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


#Feature Development:
DROP TABLE IF EXISTS usfinance.FinanceTrajectorFeaturePart1_Credit;
CREATE TABLE usfinance.FinanceTrajectorFeaturePart1_Credit AS 

SELECT 
    count(distinct (
    CASE WHEN page_name contains("基金") OR page_name contains("保险") OR page_name contains("理财") OR page_name contains("零钱宝") THEN pv_id END 
    )) AS visit_7days_times_financing,
    count(distinct (
    CASE WHEN page_name contains("基金") OR page_name contains("保险") OR page_name contains("理财") OR page_name contains("零钱宝") THEN substr(clct_date, 1, 10) END 
    )) AS visit_7days_days_financing,
    count(distinct (
    CASE WHEN page_name contains("充值") THEN pv_id END 
    )) AS visit_7days_times_recharge, 
    count(distinct (
    CASE WHEN page_name contains("充值") THEN substr(clct_ts, 1, 10) END 
    )) AS visit_7days_days_recharge,     
    count(distinct (
    CASE WHEN page_name contains("")
        ))   
FROM 
(SELECT *, 
    substr(clct_ts, 1, 10) AS clct_date
FROM usfinance.FinanceTrajectoryFeatureMainTB_Credit
WHERE 
    (substr(page_in_time, 1, 10) = substr(page_out_time, 1, 10)
    OR 
    unix_timestamp(page_out_time) - unix_timestamp(page_in_time) <= 86400)
    AND 
    (datediff(loan_date, page_out_time) <= 7
    OR
    datediff(loan_date, page_in_time) <= 7
    OR 
    datediff(loan_date, clct_ts) <= 7
    	)
    AND 
    pv_id IS NOT NULL 
    AND spv_uv_flg != 1
    ) 
GROUP BY 
    cust_ids, loan_no;



SELECT
    *,
    if(mod(pay_amt + 1, 100) = 0 or mod(pay_amt + 2, 100) = 0, 1.0, 0,0) AS isLikeBet,
    if()




select * 
from
(
select 
substr(opp_cert_no, 1, 18) as credit_no,
tr_tm,
tr_amt, 
fund_use,
opp_name,
'cash_im' AS flag,
prof_type
FROM fdm_dpa.s022_sfamls_t2a_trans_d
where curr_cd = 'CNY'
)





IF(ABS(pay_amt - 100) < 0.001 
OR ABS(pay_amt - 200) < 0.001
OR ABS(pay_amt - 300) < 0.001
OR ABS(pay_amt - 500) < 0.001)


















