create schema giraffe;

create table giraffe.metric
(
    id              serial primary key,
    name            varchar(255) not null unique,
    description     text
);

comment on table giraffe.metric is 'Metric dictionary';

create table giraffe.metric_value
(
    id              bigserial primary key,
    db_timestamp    timestamp(0) not null,
    local_timestamp timestamp(0) not null default current_timestamp,
    cluster         varchar(255) not null,
    db              varchar(255) not null,
    /* There is not foreign key constraint from metric_value to metric(id) in
       order not to slow down updates and deletes on table metric */
    metric_id       integer not null,
    integer_value   bigint,
    numeric_value   numeric
);

comment on table giraffe.metric_value is 'Metric values';