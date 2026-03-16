select distinct lower(regexp_replace(m.uuid_member_id, '(.{8})(.{4})(.{4})(.{4})(.{12})', '\1-\2-\3-\4-\5')) memberId, a.uii_acct_id||a.uii_acct_ext account, 
lower(regexp_replace(t.uuid_traunch_id, '(.{8})(.{4})(.{4})(.{4})(.{12})', '\1-\2-\3-\4-\5')) planId, t.branding,
lower(regexp_replace(b.uuid_bnk_id, '(.{8})(.{4})(.{4})(.{4})(.{12})', '\1-\2-\3-\4-\5')) bankId
from tu_acct a, tu_member m, tu_traunch t, tu_bank b, tu_person p, ta_login l, ta_app_context c
where a.traunch_id = '100014'
and m.web_registered = 'Y'
and a.reg_type = 'R'
and a.acct_state = '91'
and l.login_id = c.login_id
and a.uii_member_id = c.app_member_id
and l.username like 'TEST_%'
and a.seq_part_id = p.seq_person_id
and p.stopmail is null
and a.uii_member_id = m.uii_member_id
and a.uii_member_id = b.uii_member_id
and b.status = 'G'
and b.withdrawal_eligible = 'Y'
and b.ctl_ins_dttm < sysdate - 14
and a.traunch_id = t.traunch_id
and not exists (select 1 from tu_fin_txn f where f.ctl_rec_stat not in ('R', 'J', 'X') and a.seq_acct_id = f.seq_acct_id)
and not exists (select 1 from tu_acct_constraint c where a.seq_acct_id = c.seq_acct_id and (ctl_rec_stat is null or ctl_rec_stat = 'A'))
and exists (select 1 from tu_fund_balance f where a.seq_acct_id = f.seq_acct_id and f.total_units > 1000);

select memberId, account, planId, branding, bankId
from (
    select distinct 
        lower(regexp_replace(m.uuid_member_id, '(.{8})(.{4})(.{4})(.{4})(.{12})', '\1-\2-\3-\4-\5')) memberId, 
        a.uii_acct_id||a.uii_acct_ext account, 
        lower(regexp_replace(t.uuid_traunch_id, '(.{8})(.{4})(.{4})(.{4})(.{12})', '\1-\2-\3-\4-\5')) planId, 
        t.branding,
        lower(regexp_replace(b.uuid_bnk_id, '(.{8})(.{4})(.{4})(.{4})(.{12})', '\1-\2-\3-\4-\5')) bankId,
        ROW_NUMBER() OVER (PARTITION BY a.traunch_id ORDER BY a.uii_acct_id) as rn
    from tu_acct a, tu_member m, tu_traunch t, tu_bank b, tu_person p, ta_login l, ta_app_context c
    where a.traunch_id IN ('100014', '100003', '100009', '100061', '100007')
    and m.web_registered = 'Y'
    and a.reg_type = 'R'
    and a.acct_state = '91'
    and l.login_id = c.login_id
    and a.uii_member_id = c.app_member_id
    and l.username like 'TEST_%'
    and a.seq_part_id = p.seq_person_id
    and p.stopmail is null
    and a.uii_member_id = m.uii_member_id
    and a.uii_member_id = b.uii_member_id
    and b.status = 'G'
    and b.withdrawal_eligible = 'Y'
    and b.ctl_ins_dttm < sysdate - 14
    and a.traunch_id = t.traunch_id
    and not exists (select 1 from tu_fin_txn f where f.ctl_rec_stat not in ('R', 'J', 'X') and a.seq_acct_id = f.seq_acct_id)
    and not exists (select 1 from tu_acct_constraint c where a.seq_acct_id = c.seq_acct_id and (ctl_rec_stat is null or ctl_rec_stat = 'A'))
    and exists (select 1 from tu_fund_balance f where a.seq_acct_id = f.seq_acct_id and f.total_units > 1000)
) ranked
where rn <= 20;
