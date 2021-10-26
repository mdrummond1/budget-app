-- Table: public.transactions

-- DROP TABLE IF EXISTS public.transactions;

CREATE TABLE IF NOT EXISTS public.transactions
(
    transaction_id bigint NOT NULL DEFAULT nextval('transactions_transaction_ids_seq'::regclass),
    transaction_type integer,
    category_id integer,
    vendor_id integer,
    amount money NOT NULL,
    date_purchased date NOT NULL,
    memo character varying(150) COLLATE pg_catalog."default",
    CONSTRAINT transactions_pkey PRIMARY KEY (transaction_id),
    CONSTRAINT transactions_category_id_fkey FOREIGN KEY (category_id)
        REFERENCES public.categories (category_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT transactions_transaction_type_fkey FOREIGN KEY (transaction_type)
        REFERENCES public.transaction_types (transaction_type_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT transactions_vendor_id_fkey FOREIGN KEY (vendor_id)
        REFERENCES public.vendors (vendor_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.transactions
    OWNER to postgres;

GRANT DELETE, INSERT, SELECT, UPDATE ON TABLE public.transactions TO app;

GRANT ALL ON TABLE public.transactions TO postgres;

-- Trigger: ensure_transactions_correct

-- DROP TRIGGER IF EXISTS ensure_transactions_correct ON public.transactions;

CREATE TRIGGER ensure_transactions_correct
    BEFORE INSERT OR UPDATE OF transaction_type, amount
    ON public.transactions
    FOR EACH ROW
    EXECUTE FUNCTION public.edit_transactions();

-- Trigger: update_category_actual_amount

-- DROP TRIGGER IF EXISTS update_category_actual_amount ON public.transactions;

CREATE TRIGGER update_category_actual_amount
    AFTER INSERT OR DELETE OR UPDATE OF transaction_type, amount
    ON public.transactions
    FOR EACH ROW
    EXECUTE FUNCTION public.update_categories_from_transactions();