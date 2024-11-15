PGDMP                      
    |            PoliCamisetas2    15.2    15.2 !               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    17455    PoliCamisetas2    DATABASE     �   CREATE DATABASE "PoliCamisetas2" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Colombia.1252';
     DROP DATABASE "PoliCamisetas2";
                postgres    false            �            1259    17486 	   camisetas    TABLE     �   CREATE TABLE public.camisetas (
    id integer NOT NULL,
    tipo character varying(100) NOT NULL,
    talla character varying(50) NOT NULL,
    material character varying(100) NOT NULL,
    precio numeric(10,2) NOT NULL,
    stock integer NOT NULL
);
    DROP TABLE public.camisetas;
       public         heap    postgres    false            �            1259    17485    camisetas_id_seq    SEQUENCE     �   CREATE SEQUENCE public.camisetas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.camisetas_id_seq;
       public          postgres    false    217                       0    0    camisetas_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.camisetas_id_seq OWNED BY public.camisetas.id;
          public          postgres    false    216            �            1259    17493    estampas    TABLE     �   CREATE TABLE public.estampas (
    id integer NOT NULL,
    nombre character varying(100) NOT NULL,
    artista character varying(100) NOT NULL,
    precio numeric(10,2) NOT NULL,
    stock integer NOT NULL
);
    DROP TABLE public.estampas;
       public         heap    postgres    false            �            1259    17492    estampas_id_seq    SEQUENCE     �   CREATE SEQUENCE public.estampas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.estampas_id_seq;
       public          postgres    false    219                       0    0    estampas_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.estampas_id_seq OWNED BY public.estampas.id;
          public          postgres    false    218            �            1259    17500    pedidos    TABLE     �   CREATE TABLE public.pedidos (
    id integer NOT NULL,
    usuario_id integer NOT NULL,
    fecha_pedido date NOT NULL,
    total numeric(10,2) NOT NULL,
    estado character varying(50) NOT NULL
);
    DROP TABLE public.pedidos;
       public         heap    postgres    false            �            1259    17499    pedidos_id_seq    SEQUENCE     �   CREATE SEQUENCE public.pedidos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.pedidos_id_seq;
       public          postgres    false    221                        0    0    pedidos_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.pedidos_id_seq OWNED BY public.pedidos.id;
          public          postgres    false    220            �            1259    17475    usuarios    TABLE     �   CREATE TABLE public.usuarios (
    id integer NOT NULL,
    nombre character varying(100) NOT NULL,
    correo character varying(100) NOT NULL,
    "contraseña" character varying(255) NOT NULL,
    rol character varying(50) NOT NULL
);
    DROP TABLE public.usuarios;
       public         heap    postgres    false            �            1259    17474    usuarios_id_seq    SEQUENCE     �   CREATE SEQUENCE public.usuarios_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.usuarios_id_seq;
       public          postgres    false    215            !           0    0    usuarios_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.usuarios_id_seq OWNED BY public.usuarios.id;
          public          postgres    false    214            u           2604    17506    camisetas id    DEFAULT     l   ALTER TABLE ONLY public.camisetas ALTER COLUMN id SET DEFAULT nextval('public.camisetas_id_seq'::regclass);
 ;   ALTER TABLE public.camisetas ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    217    216    217            v           2604    17507    estampas id    DEFAULT     j   ALTER TABLE ONLY public.estampas ALTER COLUMN id SET DEFAULT nextval('public.estampas_id_seq'::regclass);
 :   ALTER TABLE public.estampas ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    218    219    219            w           2604    17508 
   pedidos id    DEFAULT     h   ALTER TABLE ONLY public.pedidos ALTER COLUMN id SET DEFAULT nextval('public.pedidos_id_seq'::regclass);
 9   ALTER TABLE public.pedidos ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    220    221    221            t           2604    17509    usuarios id    DEFAULT     j   ALTER TABLE ONLY public.usuarios ALTER COLUMN id SET DEFAULT nextval('public.usuarios_id_seq'::regclass);
 :   ALTER TABLE public.usuarios ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    214    215                      0    17486 	   camisetas 
   TABLE DATA           M   COPY public.camisetas (id, tipo, talla, material, precio, stock) FROM stdin;
    public          postgres    false    217   u#                 0    17493    estampas 
   TABLE DATA           F   COPY public.estampas (id, nombre, artista, precio, stock) FROM stdin;
    public          postgres    false    219   �#                 0    17500    pedidos 
   TABLE DATA           N   COPY public.pedidos (id, usuario_id, fecha_pedido, total, estado) FROM stdin;
    public          postgres    false    221   $                 0    17475    usuarios 
   TABLE DATA           J   COPY public.usuarios (id, nombre, correo, "contraseña", rol) FROM stdin;
    public          postgres    false    215   >$       "           0    0    camisetas_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.camisetas_id_seq', 4, true);
          public          postgres    false    216            #           0    0    estampas_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.estampas_id_seq', 2, true);
          public          postgres    false    218            $           0    0    pedidos_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.pedidos_id_seq', 3, true);
          public          postgres    false    220            %           0    0    usuarios_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.usuarios_id_seq', 7, true);
          public          postgres    false    214            }           2606    17491    camisetas camisetas_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.camisetas
    ADD CONSTRAINT camisetas_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.camisetas DROP CONSTRAINT camisetas_pkey;
       public            postgres    false    217                       2606    17498    estampas estampas_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.estampas
    ADD CONSTRAINT estampas_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.estampas DROP CONSTRAINT estampas_pkey;
       public            postgres    false    219            �           2606    17505    pedidos pedidos_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.pedidos
    ADD CONSTRAINT pedidos_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.pedidos DROP CONSTRAINT pedidos_pkey;
       public            postgres    false    221            y           2606    17484    usuarios usuarios_correo_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_correo_key UNIQUE (correo);
 F   ALTER TABLE ONLY public.usuarios DROP CONSTRAINT usuarios_correo_key;
       public            postgres    false    215            {           2606    17482    usuarios usuarios_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.usuarios DROP CONSTRAINT usuarios_pkey;
       public            postgres    false    215               5   x�3�tN��,N-IT�/K-*29}9s��So��44ճ��440������ bZ         7   x�3�t-.I�-HTpL*.)JL.I��M,�V����+���4�Գ��46������ n��         -   x�3�4�4202�54�52崴Գ��L��-�I-IL������ � a         �   x���=
1F�S�	R��Y(6Z�
a�2�I��{#ϰ3hee�>�ޛöT9S��#:�QT��u$��r�p�b8j9Ś���";rA�����q�AK���ӓ�70�J���Q8K헫� {�|­��^ث�*x2��&Fd     