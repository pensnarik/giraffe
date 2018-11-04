CREATE TABLE IF NOT EXISTS public.migrations (
    seq SERIAL PRIMARY KEY,
    op TEXT NOT NULL
);

INSERT INTO public.migrations (op) VALUES ('beforeAll 00_create_database_ops.sql');
