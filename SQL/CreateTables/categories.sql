-- Table: public.categories

-- DROP TABLE IF EXISTS public.categories;

CREATE TABLE IF NOT EXISTS public.categories
(
    category_id integer NOT NULL DEFAULT nextval('categories_category_id_seq'::regclass),
    category_type integer,
    budget_id integer,
    category_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    budgeted_amount money NOT NULL,
    actual_total money DEFAULT '$0.00'::money,
    amount_difference money GENERATED ALWAYS AS ((budgeted_amount - actual_total)) STORED,
    CONSTRAINT categories_pkey PRIMARY KEY (category_id),
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

-- Trigger: update_budgets_from_categories_tgr

-- DROP TRIGGER IF EXISTS update_budgets_from_categories_tgr ON public.categories;

CREATE TRIGGER update_budgets_from_categories_tgr
    BEFORE INSERT OR DELETE OR UPDATE OF category_type, actual_total
    ON public.categories
    FOR EACH STATEMENT
    EXECUTE FUNCTION public.update_budgets_from_categories();