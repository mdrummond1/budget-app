-- Table: public.budgets

-- DROP TABLE IF EXISTS public.budgets;

CREATE TABLE IF NOT EXISTS public.budgets
(
    budget_id integer NOT NULL DEFAULT nextval('budgets_budget_id_seq'::regclass),
    budget_start_date date NOT NULL,
    budget_end_date date GENERATED ALWAYS AS ((budget_start_date + '30 days'::interval)) STORED,
    total_income money,
    total_liability money,
    net_amount money GENERATED ALWAYS AS ((total_income + total_liability)) STORED,
    CONSTRAINT budgets_pkey PRIMARY KEY (budget_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.budgets
    OWNER to postgres;

GRANT UPDATE, INSERT, SELECT ON TABLE public.budgets TO app;

GRANT ALL ON TABLE public.budgets TO postgres;