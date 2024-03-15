--
-- PostgreSQL database dump
--

-- Dumped from database version 14.11 (Ubuntu 14.11-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.11 (Ubuntu 14.11-0ubuntu0.22.04.1)

-- Started on 2024-03-15 15:31:45 EAT

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 209 (class 1259 OID 16425)
-- Name: test_roi_tbl; Type: TABLE; Schema: public; Owner: nkoech
--

CREATE TABLE public.test_roi_tbl (
    image_date date,
    min double precision,
    max double precision,
    mean double precision,
    median double precision,
    std_dev double precision
);


ALTER TABLE public.test_roi_tbl OWNER TO nkoech;

--
-- TOC entry 3345 (class 0 OID 16425)
-- Dependencies: 209
-- Data for Name: test_roi_tbl; Type: TABLE DATA; Schema: public; Owner: nkoech
--

COPY public.test_roi_tbl (image_date, min, max, mean, median, std_dev) FROM stdin;
2024-03-15	-0.05908976495265961	0.6738551259040833	0.4945444133424539	0.5072463750839233	0.06412473830772163
2024-03-15	-0.6188784837722778	0.06144971027970314	-0.42755065074164744	-0.4367622137069702	0.06276932215864407
2024-03-15	-17620	15060	4.053278536039713	4.182857513427734	172.1729614260082
\.


-- Completed on 2024-03-15 15:31:49 EAT

--
-- PostgreSQL database dump complete
--

