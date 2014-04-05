--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone NOT NULL,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(75) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO postgres;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    content_type_id integer,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: django_site; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.django_site OWNER TO postgres;

--
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_site_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_site_id_seq OWNER TO postgres;

--
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_site_id_seq OWNED BY django_site.id;


--
-- Name: pet_blog; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE pet_blog (
    id integer NOT NULL,
    author_id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    title character varying(100) NOT NULL,
    story_description character varying(255) NOT NULL,
    story character varying(5000) NOT NULL,
    picture character varying(100) NOT NULL,
    slug character varying(50) NOT NULL,
    link character varying(200) NOT NULL
);


ALTER TABLE public.pet_blog OWNER TO postgres;

--
-- Name: pet_blog_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE pet_blog_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pet_blog_id_seq OWNER TO postgres;

--
-- Name: pet_blog_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE pet_blog_id_seq OWNED BY pet_blog.id;


--
-- Name: pet_contact; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE pet_contact (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    message character varying(1500) NOT NULL,
    subject character varying(100) NOT NULL
);


ALTER TABLE public.pet_contact OWNER TO postgres;

--
-- Name: pet_contact_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE pet_contact_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pet_contact_id_seq OWNER TO postgres;

--
-- Name: pet_contact_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE pet_contact_id_seq OWNED BY pet_contact.id;


--
-- Name: pet_indexphoto; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE pet_indexphoto (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    name character varying(55) NOT NULL,
    picture character varying(100) NOT NULL,
    slogan character varying(255) NOT NULL
);


ALTER TABLE public.pet_indexphoto OWNER TO postgres;

--
-- Name: pet_indexphoto_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE pet_indexphoto_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pet_indexphoto_id_seq OWNER TO postgres;

--
-- Name: pet_indexphoto_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE pet_indexphoto_id_seq OWNED BY pet_indexphoto.id;


--
-- Name: pet_kennel; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE pet_kennel (
    id integer NOT NULL,
    name character varying(55) NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    salt character varying(75) NOT NULL,
    short_salt character varying(75) NOT NULL,
    slug character varying(50) NOT NULL,
    manager_id integer NOT NULL,
    kennel_name character varying(75) NOT NULL,
    contact character varying(50) NOT NULL,
    info character varying(1000) NOT NULL,
    picture character varying(100),
    email character varying(100) NOT NULL,
    newsletter boolean NOT NULL
);


ALTER TABLE public.pet_kennel OWNER TO postgres;

--
-- Name: pet_kennel_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE pet_kennel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pet_kennel_id_seq OWNER TO postgres;

--
-- Name: pet_kennel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE pet_kennel_id_seq OWNED BY pet_kennel.id;


--
-- Name: pet_kennel_owners; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE pet_kennel_owners (
    id integer NOT NULL,
    kennel_id integer NOT NULL,
    owner_id integer NOT NULL
);


ALTER TABLE public.pet_kennel_owners OWNER TO postgres;

--
-- Name: pet_kennel_owners_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE pet_kennel_owners_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pet_kennel_owners_id_seq OWNER TO postgres;

--
-- Name: pet_kennel_owners_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE pet_kennel_owners_id_seq OWNED BY pet_kennel_owners.id;


--
-- Name: pet_newsletter; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE pet_newsletter (
    id integer NOT NULL,
    email character varying(100) NOT NULL
);


ALTER TABLE public.pet_newsletter OWNER TO postgres;

--
-- Name: pet_newsletter_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE pet_newsletter_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pet_newsletter_id_seq OWNER TO postgres;

--
-- Name: pet_newsletter_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE pet_newsletter_id_seq OWNED BY pet_newsletter.id;


--
-- Name: pet_owner; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE pet_owner (
    id integer NOT NULL,
    name character varying(55) NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    salt character varying(75) NOT NULL,
    short_salt character varying(75) NOT NULL,
    slug character varying(50) NOT NULL,
    owner_id integer NOT NULL,
    contact character varying(50) NOT NULL,
    info character varying(1000) NOT NULL,
    picture character varying(100),
    email character varying(100) NOT NULL,
    newsletter boolean NOT NULL
);


ALTER TABLE public.pet_owner OWNER TO postgres;

--
-- Name: pet_owner_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE pet_owner_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pet_owner_id_seq OWNER TO postgres;

--
-- Name: pet_owner_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE pet_owner_id_seq OWNED BY pet_owner.id;


--
-- Name: pet_owner_pets; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE pet_owner_pets (
    id integer NOT NULL,
    owner_id integer NOT NULL,
    pet_id integer NOT NULL
);


ALTER TABLE public.pet_owner_pets OWNER TO postgres;

--
-- Name: pet_owner_pets_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE pet_owner_pets_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pet_owner_pets_id_seq OWNER TO postgres;

--
-- Name: pet_owner_pets_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE pet_owner_pets_id_seq OWNED BY pet_owner_pets.id;


--
-- Name: pet_pet; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE pet_pet (
    id integer NOT NULL,
    name character varying(55) NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    salt character varying(75) NOT NULL,
    short_salt character varying(75) NOT NULL,
    slug character varying(50) NOT NULL,
    food character varying(1000) NOT NULL,
    emergency character varying(1000) NOT NULL,
    age integer,
    care character varying(1000) NOT NULL,
    walk character varying(1000) NOT NULL,
    picture character varying(100),
    house_trained boolean NOT NULL,
    spayed_or_neutered boolean NOT NULL,
    barks boolean NOT NULL,
    CONSTRAINT pet_pet_age_check CHECK ((age >= 0))
);


ALTER TABLE public.pet_pet OWNER TO postgres;

--
-- Name: pet_pet_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE pet_pet_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pet_pet_id_seq OWNER TO postgres;

--
-- Name: pet_pet_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE pet_pet_id_seq OWNED BY pet_pet.id;


--
-- Name: south_migrationhistory; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE south_migrationhistory (
    id integer NOT NULL,
    app_name character varying(255) NOT NULL,
    migration character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.south_migrationhistory OWNER TO postgres;

--
-- Name: south_migrationhistory_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE south_migrationhistory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.south_migrationhistory_id_seq OWNER TO postgres;

--
-- Name: south_migrationhistory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE south_migrationhistory_id_seq OWNED BY south_migrationhistory.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_site ALTER COLUMN id SET DEFAULT nextval('django_site_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY pet_blog ALTER COLUMN id SET DEFAULT nextval('pet_blog_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY pet_contact ALTER COLUMN id SET DEFAULT nextval('pet_contact_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY pet_indexphoto ALTER COLUMN id SET DEFAULT nextval('pet_indexphoto_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY pet_kennel ALTER COLUMN id SET DEFAULT nextval('pet_kennel_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY pet_kennel_owners ALTER COLUMN id SET DEFAULT nextval('pet_kennel_owners_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY pet_newsletter ALTER COLUMN id SET DEFAULT nextval('pet_newsletter_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY pet_owner ALTER COLUMN id SET DEFAULT nextval('pet_owner_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY pet_owner_pets ALTER COLUMN id SET DEFAULT nextval('pet_owner_pets_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY pet_pet ALTER COLUMN id SET DEFAULT nextval('pet_pet_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY south_migrationhistory ALTER COLUMN id SET DEFAULT nextval('south_migrationhistory_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group (id, name) FROM stdin;
1	Owner Users
2	Kennel Users
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_id_seq', 2, true);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	1	39
2	2	40
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 2, true);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add permission	1	add_permission
2	Can change permission	1	change_permission
3	Can delete permission	1	delete_permission
4	Can add group	2	add_group
5	Can change group	2	change_group
6	Can delete group	2	delete_group
7	Can add user	3	add_user
8	Can change user	3	change_user
9	Can delete user	3	delete_user
10	Can add content type	4	add_contenttype
11	Can change content type	4	change_contenttype
12	Can delete content type	4	delete_contenttype
13	Can add session	5	add_session
14	Can change session	5	change_session
15	Can delete session	5	delete_session
16	Can add site	6	add_site
17	Can change site	6	change_site
18	Can delete site	6	delete_site
19	Can add log entry	7	add_logentry
20	Can change log entry	7	change_logentry
21	Can delete log entry	7	delete_logentry
22	Can add migration history	8	add_migrationhistory
23	Can change migration history	8	change_migrationhistory
24	Can delete migration history	8	delete_migrationhistory
25	Can add pet	9	add_pet
26	Can change pet	9	change_pet
27	Can delete pet	9	delete_pet
28	Can add owner	10	add_owner
29	Can change owner	10	change_owner
30	Can delete owner	10	delete_owner
31	Is Owner	10	is_owner
32	Can add kennel	11	add_kennel
33	Can change kennel	11	change_kennel
34	Can delete kennel	11	delete_kennel
35	Is Kennel	11	is_kennel
36	Can add contact	12	add_contact
37	Can change contact	12	change_contact
38	Can delete contact	12	delete_contact
39	Is Owner	10	is_a_owner
40	Is Kennel	11	is_a_kennel
41	Can add newsletter	13	add_newsletter
42	Can change newsletter	13	change_newsletter
43	Can delete newsletter	13	delete_newsletter
44	Can add blog	14	add_blog
45	Can change blog	14	change_blog
46	Can delete blog	14	delete_blog
47	Is Blogger	14	is_blogger
48	Can add index photo	15	add_indexphoto
49	Can change index photo	15	change_indexphoto
50	Can delete index photo	15	delete_indexphoto
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_permission_id_seq', 50, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
5	md5$nZSeIFy7Yh9T$2b00279c28da856e0c9d456a91c6900a	2013-12-05 15:29:22.082587-08	f	Dad			pyaaron@gmail.com	f	t	2013-12-05 15:29:22.082587-08
6	md5$8itMqDVKxiic$03379f42e7d8e70c642fcf6cbeb402c2	2013-12-05 15:29:22.086592-08	f	Miles			pyaaron@gmail.com	f	t	2013-12-05 15:29:22.086592-08
1	md5$7YGsF0sZxNC9$6308833f75c129bc60776a1512c21627	2013-12-19 07:08:46.675389-08	t	Aaron			pyaaron@gmail.com	t	t	2013-12-05 15:28:36.375816-08
4	md5$uDTNEPiQN07i$9a82bb77733949323dd7f28d579607f2	2013-12-06 15:12:43.980087-08	f	Lauren			pyaaron@gmail.com	f	t	2013-12-05 15:29:22.078718-08
2	md5$A1RUtHAJXy8S$a71f98c9f25840f9cf21767caa3934ee	2013-12-21 19:32:05.037996-08	f	Evelyn			pyaaron@gmail.com	f	t	2013-12-05 15:29:22.031371-08
7	md5$l7LAiLEGnIQx$98647e52e713a743c4fedc79bfa58581	2013-12-07 13:05:50.147216-08	f	Jordan4			pyaaron@gmail.com	f	t	2013-12-06 15:17:22.012333-08
3	md5$AFfAXfiYhAKj$0d20cda639867a541476114cafbae096	2013-12-22 18:05:01.606595-08	f	Yuki			pyaaron@gmail.com	f	t	2013-12-05 15:29:22.074621-08
8	md5$YuYDMILnhsHY$d19b3120809255d54206b150a48e70df	2013-12-07 14:05:48.844604-08	f	Jordan5			pyaaron@gmail.com	f	t	2013-12-07 13:06:52.941795-08
9	md5$RHC5JO6G14my$723eeceb4a3e05f4844e323c9f855270	2013-12-08 18:46:30.007102-08	f	Newsletter_User			pyaaron@gmail.com	f	t	2013-12-08 18:46:30.007102-08
10	md5$2FxzdJgiH6ZK$c08ac38b95c809e018edf5b8395f57d5	2013-12-08 18:48:44.609867-08	f	Newsletter_User2			pyaaron@gmail.com	f	t	2013-12-08 18:48:44.609867-08
11	md5$aYa8ItchHNLz$c631e2e7c61f8f0ace9a578be46dac50	2013-12-08 18:51:17.386677-08	f	Newsletter_User3			pyaaron@gmail.com	f	t	2013-12-08 18:51:17.386677-08
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
1	3	1
2	4	1
3	2	2
4	7	1
5	8	1
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 5, true);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_id_seq', 11, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_admin_log (id, action_time, user_id, content_type_id, object_id, object_repr, action_flag, change_message) FROM stdin;
1	2013-12-18 07:33:58.720825-08	1	14	1	Cute Canine Brothers	1	
2	2013-12-18 07:37:03.862094-08	1	14	2	Man Tricked in Pet Purchase	1	
3	2013-12-18 07:39:21.71253-08	1	14	3	Dog Rescued	1	
4	2013-12-19 07:09:44.390909-08	1	15	1	pet_pals	1	
5	2013-12-19 07:22:56.176787-08	1	15	1	pet_pals	2	Changed slogan.
6	2013-12-19 07:24:00.249012-08	1	15	2	maltese_puppy	1	
7	2013-12-19 07:25:03.650858-08	1	15	3	dog_and_cat_friends	1	
8	2013-12-19 07:35:11.311742-08	1	15	3	dog_and_cat_friends	2	Changed picture.
9	2013-12-19 07:35:21.171001-08	1	15	2	maltese_puppy	2	Changed picture.
10	2013-12-19 07:35:39.436309-08	1	15	1	pet_pals	2	Changed picture.
11	2013-12-19 07:36:13.845365-08	1	15	2	boo_the_sad_bear	2	Changed name.
12	2013-12-19 07:37:57.684668-08	1	15	1	pet_pals	2	Changed picture.
13	2013-12-19 07:44:26.395962-08	1	15	1	pet_pals	2	Changed picture.
14	2013-12-19 07:46:45.895081-08	1	15	3	dog_and_cat_friends	2	No fields changed.
15	2013-12-19 07:47:16.629665-08	1	15	3	dog_and_cat_friends	2	Changed picture.
16	2013-12-20 07:35:37.677963-08	1	14	1	Cute Canine Brothers	2	Changed link.
17	2013-12-20 07:36:39.453144-08	1	14	3	Dog Rescued	2	Changed link.
18	2013-12-20 07:37:28.348357-08	1	14	2	Man Tricked in Pet Purchase	2	Changed link.
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 18, true);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_content_type (id, name, app_label, model) FROM stdin;
1	permission	auth	permission
2	group	auth	group
3	user	auth	user
4	content type	contenttypes	contenttype
5	session	sessions	session
6	site	sites	site
7	log entry	admin	logentry
8	migration history	south	migrationhistory
9	pet	pet	pet
10	owner	pet	owner
11	kennel	pet	kennel
12	contact	pet	contact
13	newsletter	pet	newsletter
14	blog	pet	blog
15	index photo	pet	indexphoto
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_content_type_id_seq', 15, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
5hs8qqr2hasbnufkzocapbn8ov2ddain	NjA0ZWVmOTU3M2ZhZTNlZDI1OWQyODIzNzNmOTljNDVmZjNhZGQyMjp7fQ==	2014-01-05 18:09:47.169703-08
\.


--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_site (id, domain, name) FROM stdin;
1	example.com	example.com
\.


--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_site_id_seq', 1, true);


--
-- Data for Name: pet_blog; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY pet_blog (id, author_id, created, modified, title, story_description, story, picture, slug, link) FROM stdin;
1	1	2013-12-18 07:33:58.715109-08	2013-12-20 07:35:37.672832-08	Cute Canine Brothers	Cute canine brothers Jeffrey and Jermaine melt internet's heart	IF YOU thought this pair of cute canines were the sweetest thing on the internet, wait until you read their story.\r\nEight -month-old brothers Jermaine and Jeffrey were found lost and homeless on the streets of Philadelphia in October and animal rescue centre Chester County SPCA are keen to keep them together and adopt them out as a pair.\r\nJeffrey is blind, and Jermaine ferries him around acting as his own brotherly guide dog.\r\nIn a Facebook post which has so far received more than 75,000 shares, Chester County writes: "Pictures are worth a thousand words, but this one might just leave you speechless.\r\n"Jermaine ... has dedicated his life to be Jeffrey's loyal guide dog. Here they are as they sleep, holding on to each other. The unconditional love and devotion these two dogs show is positively inspirational."\r\nIt gets better, with the news there is a chance Jeffrey's vision loss could be healed. The shelter believes the blindness is a congenital or birth condition.	manager_pictures/pit bulls hugging.jpg	cute-canine-brothers	http://www.news.com.au/lifestyle/home/cute-canine-brothers-jeffrey-and-jermaine-melt-internets-heart/story-fngwib2y-1226764056996
3	1	2013-12-18 07:39:21.708178-08	2013-12-20 07:36:39.450943-08	Dog Rescued	Dog rescued from house fire in Golden Hill	A dog was rescued from a two-story home in Golden Hill that caught on fire Wednesday around noon.\r\n\r\nThe Victorian-style home was in the 900 block of 22nd street.\r\n\r\nA woman that was home when the fire started said that she discovered the fire when she went into her kitchen. She lives with her three kids and husband, who were not home at the time. The home also has a couple of small apartments and a dog was rescued from one of them. The dog was given oxygen and is now doing well. No one else was in the apartments at the time of the fire.\r\n\r\nAs of 1 p.m. the fire was under control, said Maurice Luque of San Diego Fire Department.\r\n\r\nThe cause of the fire is unknown, Luque said. The cost of the damage to the home is also unknown at this time.	manager_pictures/house fire.png	dog-rescued	http://www.utsandiego.com/news/2013/Dec/11/firefighters-douse-flames-golden-hill/
2	1	2013-12-18 07:37:03.859612-08	2013-12-20 07:37:28.345744-08	Man Tricked in Pet Purchase	A Man Paid $150 For Toy Poodles That Ended Up Actually Being Huge Ferrets	A man recently discovered the two extremely cheap toy poodles he had purchased at Argentina’s largest bazaar were actually ferrets. Two huge white ferrets.\r\n\r\nThe man took his two new pets to a veterinarian to get their shots. The vet then revealed that his toy poodles were actually ferrets that had been given steroids since birth to make them look like poodles.\r\n\r\nThe undercover ferrets were purchased at La Salada, one of Argentina’s largest markets.\r\n\r\nA local news station looked into the story, and discovered that other customers have had similar experiences, buying what they thought were dogs that were actually huge ferrets.\r\n\r\nSo, if you’re ever traveling shopping in Argentina, just remember the animal on the left here is a dog, and the animal on the right is a ferret.	manager_pictures/toy poodle ferret.jpg	man-tricked-in-pet-purchase	http://www.buzzfeed.com/ryanhatesthis/a-man-paid-150-for-toy-poodles-that-ended-up-actually-being
\.


--
-- Name: pet_blog_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('pet_blog_id_seq', 3, true);


--
-- Data for Name: pet_contact; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY pet_contact (id, name, email, message, subject) FROM stdin;
1	aaron	pyaaron@gmail.com	test 3 	test
2	aaron	pyaaron@gmail.com	test with errors	test
3	John	pyaaron@gmail.com	test message	test subject
4	John	pyaaron@gmail.com	test message	test subject
5	John	pyaaron@gmail.com	test message	test subject
\.


--
-- Name: pet_contact_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('pet_contact_id_seq', 5, true);


--
-- Data for Name: pet_indexphoto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY pet_indexphoto (id, created, modified, name, picture, slogan) FROM stdin;
2	2013-12-19 07:24:00.246666-08	2013-12-19 07:36:13.843447-08	boo_the_sad_bear	index_pictures/index_Boo-The-Dog-sad_Fotor.jpg	Add and remove the people who watch your pets so you have control of who you share your pet's details with.
1	2013-12-19 07:09:44.388202-08	2013-12-19 07:44:26.392544-08	pet_pals	index_pictures/Foxteriér_a_kocúr_Fotor.jpg	Store your pets details and share them with the people who watch your pets.
3	2013-12-19 07:25:03.647715-08	2013-12-19 07:47:16.626087-08	dog_and_cat_friends	index_pictures/cute_and_funny_small_dog_wallpaper-normal_Fotor.jpg	Update your information anytime so that when your pet sitter needs it they have the most current info about your pets.
\.


--
-- Name: pet_indexphoto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('pet_indexphoto_id_seq', 3, true);


--
-- Data for Name: pet_kennel; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY pet_kennel (id, name, created, modified, salt, short_salt, slug, manager_id, kennel_name, contact, info, picture, email, newsletter) FROM stdin;
1	Evelyn Wurl	2013-12-05 15:29:22.12241-08	2013-12-21 19:32:15.662535-08	$2a$12$RzQBV8hJz0Zc/l4GUCaXhe	Xdb0lLzc	evelyn	2	Evenlyn's Kennel	123-4567	Note that each form field has an ID attribute set to id_<field-name>, which is referenced by the accompanying label tag. This is important for ensuring forms are accessible to assistive technology such as screen reader software. You can also customize the way in which labels and ids are generated.\r\n\r\nYou can also use form.as_table to output table rows (you’ll need to provide your own <table> tags) and form.as_ul to output list items.\r\n\r\nNote that each form field has an ID attribute set to id_<field-name>, which is referenced by the accompanying label tag. This is important for ensuring forms are accessible to assistive technology such as screen reader software. You can also customize 	manager_pictures/DSCN1741.JPG	pyaaron@gmail.com	t
2	Dad	2013-12-05 15:29:22.138241-08	2013-12-21 19:50:43.416959-08	$2a$12$DQ3kY0fZayfW4BCZg37tMu	gCTaddtY	dad	5	Dad's Kennel				pyaaron@gmail.com	f
\.


--
-- Name: pet_kennel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('pet_kennel_id_seq', 2, true);


--
-- Data for Name: pet_kennel_owners; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY pet_kennel_owners (id, kennel_id, owner_id) FROM stdin;
1	1	1
4	2	1
\.


--
-- Name: pet_kennel_owners_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('pet_kennel_owners_id_seq', 4, true);


--
-- Data for Name: pet_newsletter; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY pet_newsletter (id, email) FROM stdin;
1	pyaaron@gmail.com
2	aaron.yy.lelevier@gmail.com
3	pyaaron@gmail.com
\.


--
-- Name: pet_newsletter_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('pet_newsletter_id_seq', 3, true);


--
-- Data for Name: pet_owner; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY pet_owner (id, name, created, modified, salt, short_salt, slug, owner_id, contact, info, picture, email, newsletter) FROM stdin;
3	Miles	2013-12-05 15:29:22.170535-08	2013-12-05 15:29:22.170629-08	$2a$12$FW44ZJFwxq1sGPvcB98o2e	cEK7DxAV	miles	6				pyaaron@gmail.com	f
2	Lauren	2013-12-05 15:29:22.160736-08	2013-12-05 15:29:22.231422-08	$2a$12$rMxF5mv/P9xGQ05ZheEdx.	gktVXeLb	lauren	4				pyaaron@gmail.com	f
4	Jordan4	2013-12-06 15:17:22.019044-08	2013-12-06 15:17:22.019078-08	$2a$12$2bPSdn8FQzPiyBsixOD4Du	OuH6SOkJ	jordan4	7				pyaaron@gmail.com	f
5	Jordan5	2013-12-07 13:06:52.962427-08	2013-12-07 14:13:10.014975-08	$2a$12$I54ROej3QWgWUW09n3NWue	YWm1Vqyd	jordan5	8				pyaaron@gmail.com	f
1	Yuki	2013-12-05 15:29:22.147775-08	2013-12-08 18:16:33.043366-08	$2a$12$xICyExn.H4JvqHvicwZrru	96NPKsF6	yuki	3				pyaaron@gmail.com	t
\.


--
-- Name: pet_owner_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('pet_owner_id_seq', 5, true);


--
-- Data for Name: pet_owner_pets; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY pet_owner_pets (id, owner_id, pet_id) FROM stdin;
1	1	1
2	1	2
3	2	3
7	5	10
\.


--
-- Name: pet_owner_pets_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('pet_owner_pets_id_seq', 7, true);


--
-- Data for Name: pet_pet; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY pet_pet (id, name, created, modified, salt, short_salt, slug, food, emergency, age, care, walk, picture, house_trained, spayed_or_neutered, barks) FROM stdin;
2	Dino	2013-12-05 15:29:22.10212-08	2013-12-05 15:29:22.102213-08	$2a$12$xDkgHiTYDkkWTpgRmmkfie	UyUltYed	dino	dry food	tropicana	1				f	f	f
3	Hama	2013-12-05 15:29:22.106924-08	2013-12-05 15:29:22.107015-08	$2a$12$xK9gjaxNBtddbLGWCnm6c.	psExkGB4	hama	dry food	tropicana	1				f	f	f
5	Ivy	2013-12-05 15:36:52.080069-08	2013-12-05 15:36:52.080102-08	$2a$12$PN3LrrHfgX8KavblVFnah.	S1GA3xVB	ivy	food	contact me	0				f	f	f
7	Ivy	2013-12-05 15:38:20.14975-08	2013-12-05 15:38:20.149785-08	$2a$12$KXuPZkcdQKV5IicTxwvQBe	yxGBBl1A	ivy	food	contact	0				f	f	f
9	Ivy	2013-12-05 15:39:35.086254-08	2013-12-05 15:39:35.086294-08	$2a$12$soWWUmJJ3xlMwLL3Rw5.Gu	9lBItnoy	ivy	food	contact	0				f	f	f
11	Popcorn	2013-12-07 14:13:10.017579-08	2013-12-07 14:13:10.01761-08	$2a$12$FIGwLsB95YpV1ICsznqeF.	TYujMnYw	popcorn	eats	food	2			pet_pictures/DSCN1718_1.JPG	f	f	f
10	Popcorn	2013-12-07 14:13:09.981223-08	2013-12-07 14:14:49.544675-08	$2a$12$M.u0ip2JOVKpAI9dUjy2Pe	jDJs5Ea5	popcorn	eats	food	2			pet_pictures/DSCN1718.JPG	f	f	f
1	Bobbi	2013-12-05 15:29:22.095316-08	2013-12-21 19:32:48.383595-08	$2a$12$Bi8xQoV01Fhi3O7BmWEEcO	a6MaDx3h	bobbi	dry food	tropicana	1	Note that each form field has an ID attribute set to id_<field-name>, which is referenced by the accompanying label tag. This is important for ensuring forms are accessible to assistive technology such as screen reader software. You can also customize the way in which labels and ids are generated.\r\n\r\nYou can also use form.as_table to output table rows (you’ll need to provide your own <table> tags) and form.as_ul to output list items.	Note that each form field has an ID attribute set to id_<field-name>, which is referenced by the accompanying label tag. This is important for ensuring forms are accessible to assistive technology such as screen reader software. You can also customize the way in which labels and ids are generated.\r\n\r\nYou can also use form.as_table to output table rows (you’ll need to provide your own <table> tags) and form.as_ul to output list items.	pet_pictures/DSCN1739.JPG	t	f	t
\.


--
-- Name: pet_pet_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('pet_pet_id_seq', 11, true);


--
-- Data for Name: south_migrationhistory; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY south_migrationhistory (id, app_name, migration, applied) FROM stdin;
1	pet	0001_initial	2013-12-05 15:28:50.505092-08
2	pet	0002_auto__add_field_owner_email	2013-12-05 15:28:50.611392-08
3	pet	0003_auto__add_field_kennel_email	2013-12-05 15:28:50.716173-08
4	pet	0004_auto__add_contact	2013-12-05 15:28:50.829183-08
5	pet	0005_auto__del_field_contact_website__add_field_contact_subject	2013-12-08 13:54:21.111841-08
6	pet	0006_auto__add_newsletter__add_field_pet_house_trained__add_field_pet_spaye	2013-12-08 18:11:41.390128-08
7	pet	0007_auto__add_blog	2013-12-18 07:15:35.117959-08
8	pet	0008_auto__add_field_blog_slug	2013-12-18 07:22:57.540812-08
9	pet	0009_auto__add_indexphoto	2013-12-19 07:08:03.530617-08
10	pet	0010_auto__add_field_indexphoto_slogan	2013-12-19 07:20:51.721206-08
11	pet	0011_auto__add_field_indexphoto_link	2013-12-20 07:32:50.696471-08
12	pet	0012_auto__add_field_blog_link__del_field_indexphoto_link	2013-12-20 07:34:12.384345-08
\.


--
-- Name: south_migrationhistory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('south_migrationhistory_id_seq', 12, true);


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_model_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_key UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- Name: pet_blog_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY pet_blog
    ADD CONSTRAINT pet_blog_pkey PRIMARY KEY (id);


--
-- Name: pet_contact_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY pet_contact
    ADD CONSTRAINT pet_contact_pkey PRIMARY KEY (id);


--
-- Name: pet_indexphoto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY pet_indexphoto
    ADD CONSTRAINT pet_indexphoto_pkey PRIMARY KEY (id);


--
-- Name: pet_kennel_owners_kennel_id_2df430cea3e9915c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY pet_kennel_owners
    ADD CONSTRAINT pet_kennel_owners_kennel_id_2df430cea3e9915c_uniq UNIQUE (kennel_id, owner_id);


--
-- Name: pet_kennel_owners_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY pet_kennel_owners
    ADD CONSTRAINT pet_kennel_owners_pkey PRIMARY KEY (id);


--
-- Name: pet_kennel_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY pet_kennel
    ADD CONSTRAINT pet_kennel_pkey PRIMARY KEY (id);


--
-- Name: pet_newsletter_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY pet_newsletter
    ADD CONSTRAINT pet_newsletter_pkey PRIMARY KEY (id);


--
-- Name: pet_owner_pets_owner_id_2e6062aa5393e16c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY pet_owner_pets
    ADD CONSTRAINT pet_owner_pets_owner_id_2e6062aa5393e16c_uniq UNIQUE (owner_id, pet_id);


--
-- Name: pet_owner_pets_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY pet_owner_pets
    ADD CONSTRAINT pet_owner_pets_pkey PRIMARY KEY (id);


--
-- Name: pet_owner_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY pet_owner
    ADD CONSTRAINT pet_owner_pkey PRIMARY KEY (id);


--
-- Name: pet_pet_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY pet_pet
    ADD CONSTRAINT pet_pet_pkey PRIMARY KEY (id);


--
-- Name: south_migrationhistory_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY south_migrationhistory
    ADD CONSTRAINT south_migrationhistory_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_group_name_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_group_permissions_group_id ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_group_permissions_permission_id ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_permission_content_type_id ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_groups_group_id ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_groups_user_id ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_permission_id ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_user_id ON auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_username_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_admin_log_content_type_id ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_admin_log_user_id ON django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_session_expire_date ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_session_session_key_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: pet_blog_author_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX pet_blog_author_id ON pet_blog USING btree (author_id);


--
-- Name: pet_blog_slug; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX pet_blog_slug ON pet_blog USING btree (slug);


--
-- Name: pet_blog_slug_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX pet_blog_slug_like ON pet_blog USING btree (slug varchar_pattern_ops);


--
-- Name: pet_kennel_manager_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX pet_kennel_manager_id ON pet_kennel USING btree (manager_id);


--
-- Name: pet_kennel_owners_kennel_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX pet_kennel_owners_kennel_id ON pet_kennel_owners USING btree (kennel_id);


--
-- Name: pet_kennel_owners_owner_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX pet_kennel_owners_owner_id ON pet_kennel_owners USING btree (owner_id);


--
-- Name: pet_kennel_slug; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX pet_kennel_slug ON pet_kennel USING btree (slug);


--
-- Name: pet_kennel_slug_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX pet_kennel_slug_like ON pet_kennel USING btree (slug varchar_pattern_ops);


--
-- Name: pet_owner_owner_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX pet_owner_owner_id ON pet_owner USING btree (owner_id);


--
-- Name: pet_owner_pets_owner_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX pet_owner_pets_owner_id ON pet_owner_pets USING btree (owner_id);


--
-- Name: pet_owner_pets_pet_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX pet_owner_pets_pet_id ON pet_owner_pets USING btree (pet_id);


--
-- Name: pet_owner_slug; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX pet_owner_slug ON pet_owner USING btree (slug);


--
-- Name: pet_owner_slug_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX pet_owner_slug_like ON pet_owner USING btree (slug varchar_pattern_ops);


--
-- Name: pet_pet_slug; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX pet_pet_slug ON pet_pet USING btree (slug);


--
-- Name: pet_pet_slug_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX pet_pet_slug_like ON pet_pet USING btree (slug varchar_pattern_ops);


--
-- Name: auth_group_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: author_id_refs_id_b066660d; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY pet_blog
    ADD CONSTRAINT author_id_refs_id_b066660d FOREIGN KEY (author_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: content_type_id_refs_id_d043b34a; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT content_type_id_refs_id_d043b34a FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_content_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_fkey FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: group_id_refs_id_f4b32aac; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT group_id_refs_id_f4b32aac FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: kennel_id_refs_id_2e29ab56; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY pet_kennel_owners
    ADD CONSTRAINT kennel_id_refs_id_2e29ab56 FOREIGN KEY (kennel_id) REFERENCES pet_kennel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: manager_id_refs_id_097fc889; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY pet_kennel
    ADD CONSTRAINT manager_id_refs_id_097fc889 FOREIGN KEY (manager_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: owner_id_refs_id_41b23ca9; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY pet_owner_pets
    ADD CONSTRAINT owner_id_refs_id_41b23ca9 FOREIGN KEY (owner_id) REFERENCES pet_owner(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: owner_id_refs_id_435bc104; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY pet_kennel_owners
    ADD CONSTRAINT owner_id_refs_id_435bc104 FOREIGN KEY (owner_id) REFERENCES pet_owner(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: owner_id_refs_id_c557b1b0; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY pet_owner
    ADD CONSTRAINT owner_id_refs_id_c557b1b0 FOREIGN KEY (owner_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: pet_id_refs_id_bb5fb4fb; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY pet_owner_pets
    ADD CONSTRAINT pet_id_refs_id_bb5fb4fb FOREIGN KEY (pet_id) REFERENCES pet_pet(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_40c41112; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT user_id_refs_id_40c41112 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_4dc23c39; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT user_id_refs_id_4dc23c39 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

