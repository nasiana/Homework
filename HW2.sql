USE BAKERY;
select * from sweet;
create index item_name_idx on sweet(item_name);

use bank;
select * FROM accounts;
CREATE INDEX mult_col_idx_accounts ON accounts(account_number, account_holder_name, account_holder_surname);