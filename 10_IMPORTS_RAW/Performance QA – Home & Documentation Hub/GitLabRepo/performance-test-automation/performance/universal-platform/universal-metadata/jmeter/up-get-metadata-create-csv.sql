select branding, memberId, account
from (
    select distinct 
        t.branding, 
        lower(regexp_replace(m.uuid_member_id, '(.{8})(.{4})(.{4})(.{4})(.{12})', '\1-\2-\3-\4-\5')) memberId, 
        a.uii_acct_id||a.uii_acct_ext account,
        ROW_NUMBER() OVER (PARTITION BY a.traunch_id ORDER BY a.uii_acct_id) as rn
    from tu_acct a, tu_member m, tu_traunch t
    where a.traunch_id in ('100066', '100009', '100080', '100081', '100049')
    and m.web_registered = 'Y'
    and a.reg_type = 'R'
    and a.acct_state = '91'
    and a.uii_member_id = m.uii_member_id
    and a.traunch_id = t.traunch_id
    and exists (select 1 from tu_fund_balance f where a.seq_acct_id = f.seq_acct_id and f.total_units > 1000)
) ranked
where rn <= 20;
