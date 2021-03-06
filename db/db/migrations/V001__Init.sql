create schema giraffe authorization giraffe;

grant usage on schema giraffe to web;

set role giraffe;

create table giraffe.metric
(
    id              serial primary key,
    name            varchar(255) not null unique,
    description     text,
    dt              timestamptz not null default current_timestamp
);

comment on table giraffe.metric is 'Metric dictionary';

grant select on table giraffe.metric to web;

create table giraffe.metric_value
(
    id              bigserial primary key,
    db_timestamp    timestamptz not null,
    local_timestamp timestamptz not null default current_timestamp,
    cluster         varchar(255) not null,
    db              varchar(255) not null,
    /* There is no foreign key constraint from metric_value to metric(id) in
       order not to slow down updates and deletes on table metric */
    metric_id       integer not null,
    integer_value   bigint,
    numeric_value   numeric
);

comment on table giraffe.metric_value is 'Metric values';

grant select on table giraffe.metric_value to web;

create or replace
function giraffe.init_metric(aname varchar, adescription text) returns integer as $$
declare
    vid integer;
begin
    lock table giraffe.metric;
    select id into vid from giraffe.metric where name = aname;
    if vid is null then
        insert into giraffe.metric(name, description)
        values(aname, adescription)
        returning id into vid;
    end if;
    return vid;
end;
$$ language plpgsql security definer;

reset role;