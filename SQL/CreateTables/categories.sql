-- Table: public.categories

-- DROP TABLE IF EXISTS public.categories;

CREATE TABLE IF NOT EXISTS public.categories
(
    category_id integer NOT NULL DEFAULT nextval('categories_category_id_seq'::regclass),
    category_type integer,
    budget_id integer,
    category_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    budgeted_amount money NOT NULL,
    actual_total money,
    amount_difference money GENERATED ALWAYS AS ((budgeted_amount - actual_total)) STORED,
    CONSTRAINT categories_pkey PRIMARY KEY (category_id),
    CONSTRAINT categories_budget_id_fkey FOREIGN KEY (budget_id)
        REFERENCES public.budgets (budget_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT categories_category_type_fkey FOREIGN KEY (category_type)
        REFERENCES public.category_types (category_type_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.categories
    OWNER to postgres;

GRANT DELETE, INSERT, SELECT, UPDATE ON TABLE public.categories TO app;

GRANT ALL ON TABLE public.categories TO postgres;