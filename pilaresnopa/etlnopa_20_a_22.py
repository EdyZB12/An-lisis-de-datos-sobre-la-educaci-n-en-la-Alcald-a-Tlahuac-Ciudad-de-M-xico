print("hello word")

import pandas as pd
import csv
import logging 
import datetime 

datos = r"C:\Users\zabu\Desktop\pilaresnopa\pilaresnopa.xlsx"
limpios = r"C:\Users\zabu\Desktop\pilaresnopa\pilaresnopa_limpio2.csv"



df_26_hoja = pd.read_excel(datos, sheet_name=26, header=0)

print(df_26_hoja.info())
print(df_26_hoja.head())

def etl_nopa_2(df_26_hoja, limpios):
    try:
        def taller_limpio(valor):
            if pd.isna(valor):
                return 'unknown'
            
            valor = str(valor).strip().upper()
            
            if valor in ['TRAMITE DE LLAVE', 'TRAMITE LLAVE', 'GENERACIÓN LLAVE', 'CUENTA LLAVE']:
                return 'tramite_llave'
            
            elif valor in ['CUBO LED 3X3X3']:
                return 'cubo_led_3x3x3'
            
            elif valor in ['CONECTADO CON MIS EMOCIONES A TRAVÉS DE LA LITERATURA']:
                return 'conectando_con_mis_emociones_a_traves_de_la_literatura'
            
            elif valor in ['CONVERSATORIO']:
                return 'conversatorio'
            
            elif valor in ['CURSO PLATAFORMAS DIGITALES']:
                return 'curso_plataformas_digitales'
            
            elif valor in ['INFORMACION', 'INFORMES / USO DE COMPUTO', 'INFORMES']:
                return 'informes'
            
            elif valor in ['LECCIÓN DE GUITARRA']:
                return 'leccion_de_guitarra'
            
            elif valor in ['LECTOESCRITURA']:
                return 'LECTOESCRITURA'
            
            elif valor in ['LECTOESCRITURA PREESCROLAR']:
                return 'lectoescritura_preescolar'
            
            elif valor in ['LECTURA PLACENTERA(SEP)']:
                return 'lectura_placentera_sep'
            
            elif valor in ['INFORMES GENERAL']:
                return 'informes_general'
            
            elif valor in ['INFORMES BACHILLERATO']:
                return 'informes_bachillerato'
            
            elif valor in ['INFORMES BACHILLERATO EN LINEA']:
                return 'informes bachillerato en linea'
            
            elif valor in ['INFORMES COMERCIO DIGITAL']:
                return 'informes_comercio_digital'
            
            elif valor in ['INFORMES INEA']:
                return 'informes_inea'
            
            elif valor in ['INFORMES INEA SEC. ABIERTA']:
                return 'informes_inea_secundaria_abierta'
            
            elif valor in ['INFORMES PAGINAS WEB']:
                return 'informes_paginas_web'
            
            elif valor in ['INFORMES PREPA EN LINEA']:
                return 'informes_prepa_en_linea'
            
            elif valor in ['INFORMES PREPA ABIETA SEP', 'INFORMES PREPA ABIERTA']:
                return 'informes_prepa_abierta_sep'
            
            elif valor in ['INFORMES TAIC CHI']:
                return 'informes_taic_chi'
            
            elif valor in ['INFORMES TALLERES']:
                return 'informes talleres'
            
            elif valor in ['INGLES', 'INGLÉS']:
                return 'ingles'
            
            elif valor in ['INGLES 1 SABATINO 10-13']:
                return 'ingles_1_sabatino_10_a_13'
            
            elif valor in ['INGLES 1 SABATINO 14+']:
                return 'ingles_1_sabatino_14_en_adelante'
            
            elif valor in ['INGLES 2 SABATINO 14+']:
                return 'ingles_2_sabatino_14_en_adelante'
            
            elif valor in ['INGLES 7 A 9', 'INGLES 7-9 AÑOS']:
                return 'ingles_7_a_9'
            
            elif valor in ['INGLES 9 - 13']:
                return 'ingles_9_a_13'
            
            elif valor in ['INGLES 10 a 13', 'INGLES 10-13', 'INGLÉS 10-13', 'INGLES 10-13 AÑOS']:
                return 'ingles_10_a_13'
            
            elif valor in ['INGLES 10-15']:
                return 'ingles_10_a_15'
            
            elif valor in ['INGLES 14+', 'INGLÉS 14+']:
                return 'ingles_14_en_adelante'
            
            elif valor in ['ACTIVIDADES_DE_VERANO', 'ACTIVIDADES DE VERANO PILARES']:
                return 'actividades_verano'
            
            elif valor in ['ACTIVIDADES FISICO-LUDICAS']:
                return 'actividades_fisico_ludicas'
            
            elif valor in ['AJEDREZ']:
                return 'ajedrez'
            
            elif valor in ['ALGBRA:PRODUCTOS NOTABLES']:
                return 'algebra_productos_notables'
            
            elif valor in ['ASESORÍA BP LÍNEA']:
                return 'asesorias_becarios_linea'
            
            elif valor in ['ASESORIA ESPAÑOL PRIMARIA']:
                return 'asesoria_español_primaria'
            
            elif valor in ['ASESORIA INEA PRIMARIA']:
                return 'asesoria_inea_primaria'
            
            elif valor in ['ASESORÍA OTRAS UNIVERSIDADES, SALUD']:
                return 'asesoría_otras_universidades'
            
            elif valor in ['ASESORIA UNAM/BECARIO']:
                return 'asesoria_unam_becario'
            
            elif valor in ['ASESORIA/BADI']:
                return 'asesoria_badi'
            
            elif valor in ['ASESORIAS ESPAÑOL']:
                return 'asesorias_español'
            
            elif valor in ['CAMBIO DE ESCUELA']:
                return 'cambio_de_escuela'
            
            elif valor in ['CAPULLITOS DE ALGODON']:
                return 'capullitos_de_algodon'
            
            elif valor in ['CARRITO EVASOR DE OBSTÁCULOS']:
                return 'carrito_evasador_de_obstaculos'
            
            elif valor in ['CIBERESCUELA']:
                return 'ciberescuela'
            
            elif valor in ['CÍRCULO DE LECTURA Y ESCRITURA PARA MUJERES']:
                return 'circulo_de_lectura_y_escritura_para_mujeres'
            
            elif valor in ['COMERCIO DIGITAL']:
                return 'comercio_digital'
            
            elif valor in ['GUITARRA CLASICA', 'GUITARRA CLÁSICA']:
                return 'guitarra_clasica'
            
            elif valor in ['GUITARRA']:
                return 'guitarra'
            
            elif valor in ['INEA -SECUNDARIA', 'INEA SECUNDARIA']:
                return 'inea_secundaria'
            
            elif valor in ['INFORMES ASESORIA FÍSICA']:
                return 'informes_asesoria_fisica'
            
            elif valor in ['INFORMES ASESORIA MATEMATICAS', 'INFORMES MATEMATICAS, COMPUT E INGLES']:
                return 'informes_asesoria_matematicas'
            
            elif valor in ['INFORMES INGLES', 'INFORMES INGLÉS', 'INFORMES MATEMATICAS, COMPUT E INGLES']:
                return 'informes_ingles'
            
            elif valor in ['FISICA', 'FÍSICA']:
                return 'fisica'
            
            elif valor in ['GENERACION DE FOLIO', 'GENERACIÓN DE FOLIO', 'GENERAR FOLIO', 'GENERACIPON DE FOLIO']:
                return 'generacion_folio'
            
            elif valor in ['ACTIVIDADES CULTURALES', 'ACTIVIDADES DE CULTURA']:
                return 'actividades_de_cultura'
            
            elif valor in ['ASESORIAS ACADEMICAS']:
                return 'asesorias_academicas'
            
            elif valor in ['APOYO A TAREAS']:
                return 'apoyo_de_tareas'
            
            elif valor in ['APOYO A TAREAS ESPAÑOL']:
                return 'apoyo_tareas_español'
            
            elif valor in ['APOYO A TAREAS SECUNDARIA']:
                return 'apoyo_tareas_secundaria'
            
            elif valor in ['APOYO A TAREAS MATEMATICAS', 'APOYO A TAREAS MATEMÁTICAS', 'APOYO A TAREAS INTEGRALES']:
                return 'apoyo_tareas_matematicas'
            
            elif valor in ['ASESORIAS BACHILLERATO', 'ASESORÍAS BACHILLERATO', 'ASESORIA/BACHILLERATO']:
                return 'asesorias_bachillerato'
            
            elif valor in ['ASESORIA CIENCIAS NATURALES', 'ASESORÍA CIENCIAS NATURALES']:
                return 'asesorias_ciencias_naturales'
            
            elif valor in ['ASESORIA COMPUTACION', 'ASESORÍA COMPUTACION']:
                return 'asesoria_computacion'
            
            elif valor in ['ASESORÍA DE MATEMÁTICAS', 'ASESORIA DE MATEMÁTICAS', 'ASEOSRÍAS MATEMÁTICAS',
                           'ASESORÍA MATEMATICA S', 'ASESORÍA  MATEMÁTICAS', 'ASESORIA  MATEMATICAS',
                           'ASESORIA MATEMATICAS', 'ASESORÍA MATEMATICAS', 'ASESORÍA MATEMÁTICAS', 'ASESORIA/MATEMATICAS',
                           'ASESORIAS DE MATEMÁTICAS', 'ASESORIAS MATEMATICAS', 'ASESORÍAS MATEMATICAS',
                           'ASESORÍAS MATEMÁTICAS']:
                return 'asesoria_matematicas'
            
            elif valor in ['ASESORIA FISICA', 'ASESORIA FÍSICA', 'ASESORÍA FÍSICA', 'ASESORIA FISICA Y QUÍMICA',
                           'ASESORIAS FISICA', 'ASESORÍAS FISICA']:
                return 'asesoria_fisica'
            
            elif valor in ['ASESORÍA  FORMACIÓ CÍVICA Y ÉTICA', 'ASESORÍA FORMACIÒN C/E', 'ASESORÍA FORMACIÒN C/E',
                           'ASESORÍA FORMACIÒN CÌVICA Y ÈTICA']:
                return 'asesoria_formacion_civica_y_etica'
            
            elif valor in ['ASESORIA GEOGRAFIA', 'ASESORÍA GEOGRAFÍA', 'ASESORIAS GEOGRAFÍA Y CIENCIAS NATURALES',
                           'ASESORIAS CIENCIAS GEOGRAFÍA']:
                return 'asesoria_geografia'
            
            elif valor in ['ASESORIA HISTORIA', 'ASESORÍA HISTORIA', ' ASESORÌA HISTORIA', 'ASESORÍAS HISTORIA']:
                return 'asesoria_historia'
            
            elif valor in ['ASESORÍA INGLÉS', 'ASESORIA INGLES', 'INGLES-COMPUTACIÓN']:
                return 'asesoria_ingles'
            
            elif valor in ['ASESORIA MATEMATICAS BACHILLERATO', 'ASESORIA MATEMÁTICAS BACHILLERATO',
                           'ASESORÍA MATEMATICAS BACHILLERATO', 'ASESORIAS MATE BACHILLERATO',
                           'ASESORÍAS MATE BACHILLERATO', 'ASESORÍAS MATEMÁTICAS BACHILLERATO',
                           'ASESORIAS MATEMÁTICAS NIVEL BACHILLERATO']:
                return 'asesoria_matematicas_bachillerato'
            
            elif valor in ['INGLES BASICO', 'INGLES BÁSICO', 'INGLÉS BASICO', 'INGLÉS BÁSICO', 'CURSO BASICO INGLES',
                           'CURSO BÁSICO INGLÉS']:
                return 'ingles_basico'
            
            elif valor in ['INGLÉS BÁSICO 1', 'CURSO BÁSICO INGLÉS 1']:
                return 'ingles_basico_1'
            
            elif valor in ['CURSO BÁSICO INGLÉS 2', 'INGLÉS BÁSICO 2']:
                return 'curso_basico_ingles_2'
            
            elif valor in ['CURSO BÁSICO INGLÉS 3', 'INGLES BASICO 3']:
                return 'curso_basico_ingles_3'
            
            elif valor in ['CURSO BÁSICO INGLÉS 4', 'INGLES BASICO 4', 'INGLÉS BÁSICO 4']:
                return 'curso_basico_ingles_4'
            
            elif valor in ['INGLES BASICO 4 NIÑOS']:
                return 'ingles_basico_4_niños'
            
            elif valor in ['INGLES BASICO 4 NOCTURNO']:
                return 'ingles_basico_4_nocturo'
            
            elif valor in ['INGLES BASICO 5']:
                return 'ingles_basico_5'
            
            elif valor in ['INGLES BASICO 5 NIÑOS']:
                return 'ingles_basico_5_niños'
            
            elif valor in ['INGLES BASICO 5 NOCTURNO']:
                return 'ingles_basico_5_nocturo'
            
            elif valor in ['CURSO BÁSICO INGLÉS 4 NIÑOS']:
                return 'curso_basico_ingles_4_niños'
            
            elif valor in ['INGLES BASICO 6']:
                return 'ingles_basico_6'
            
            elif valor in ['INGLES BASICO 6 NIÑOS']:
                return 'ingles_basico_6_niños'
            
            elif valor in ['INGLES BASICO 6 NOCTURNO']:
                return 'ingles_basico_6_nocturno'
            
            elif valor in ['INGLES NIÑOS 1']:
                return 'ingles_niños_1'
            
            elif valor in ['INGLES NIÑOS 2']:
                return 'ingles_niños_2'
            
            elif valor in ['INGLES NIÑOS 3']:
                return 'ingles_niños_3'
            
            elif valor in ['INGLES NIÑOS 4']:
                return 'ingles_niños_4'
            
            elif valor in ['INGLES NIÑOS 6']:
                return 'ingles_niños_6'
            
            elif valor in ['INGLES NIÑOS EN LINEA 5']:
                return 'ingles_niños_en_linea_5'
            
            elif valor in ['INGLES NIÑOS EN LINEA 6']:
                return 'ingles_niños_en_linea_6'
            
            elif valor in ['ASESORIA INGLES BÁSICO']:
                return 'asesoria_ingles_basico'
            
            elif valor in ['ASESORIA INGLES SECUNDARIA']:
                return 'asesoria_ingles_secundaria'
            
            elif valor in ['ASESORIA INGRESO UNIVERSIDAD']:
                return 'asesoria_ingreso_universidad'
            
            elif valor in ['ASESORIA KINDER', 'ASESORIA PREESCOLAR']:
                return 'asesoria_kinder'
            
            elif valor in ['ASESORIA LICENCIATURA']:
                return 'asesoria_licenciatura_sin_especificar'
            
            elif valor in ['ASESORIA MATE BACHILLERATO']:
                return 'asesoria_matematicas_bachillerato'
            
            elif valor in ['ASESORIA MATEMATICAS EXAMEN UAM']:
                return 'asesoria_matematicas_examen_uam'
            
            elif valor in ['ASESORIA MATEMATICAS EXAMEN UNAM']:
                return 'asesoria_matematicas_examen_unam'
            
            elif valor in ['INGLES NOCTURNO 1']:
                return 'ingles_nocturno_1'
            
            elif valor in ['INGLES PRIMARIA', 'INGLES PRIMARIA']:
                return 'ingles_primaria'
            
            elif valor in ['INGLÉS SABADO HIBRIDO 25+']:
                return 'ingles_sabado_hibrido_25+'
            
            elif valor in ['INGLES SECUNDARIA']:
                return 'ingles_secundaria'
            
            elif valor in ['INGLES SESION UNICA SABATINA']:
                return 'ingles_sesion_unica_sabatina'
            
            elif valor in ['INGRESO A UNIVERSIDAD', 'INGRESO UNIVERSIDAD']:
                return 'ingreso_universidad'
            
            elif valor in ['INSCRIPCION A CARPINTERÍA', 'INSCRIPCION CARPINTERÍA']:
                return 'inscripcion_carpinteria'
            
            elif valor in ['ASESORIA MATEMATICAS PRIMARIA', 'ASESORIA MATEMÁTICAS PRIMARIA',
                           'ASESORIA MATÉMATICAS PRIMARIA', 'ASESORIAS DE MATEMÁTICAS PRIMARIA', 'ASESORÍAS MATE PRIMARIA',
                           'ASESORIAS MATEMATICAS PRIMARIA', 'ASESORIA MATEMÁTICAS PRIMARIA', 'ASESORÍAS MATEMÁTICAS PRIMARIA']:
                return 'asesoria_matematicas_primaria'
            
            elif valor in ['ASESORIA MATEMATICAS SECUNDARIA', 'ASESORÍA MATEMATICAS SECUNDARIA',
                           'ASESORIA SECUNDARIA MATEMATICAS', 'ASESORÍAS MATE SECUNDARIA', 'ASESORIAS MATEMATICAS SECUNDARIA',
                           'ASESORIAS MATEMATICAS SECUNDARIA', 'ASESORIAS MATEMÁTICAS SECUNDARIA', '¡DALE JAQUE A LA FACTORIZACIÓN!']:
                return 'asesoria_matematicas_secundaria'
            
            elif valor in ['ASESORIA NIVEL PRIMARIA', 'ASESORIA PRIMARIA', 'ASESORÍA PRIMARIA',
                           'ASESORIAS PRIMARIA', 'ASESORÍAS PRIMARIA', 'ASSESORIA PRIMARIA']:
                return 'asesoria_primaria_no_especificado'
            
            elif valor in ['ATENCION COLEGIO DE CIENCIAS EXACTAS']:
                return 'atencion_colegio_ciencias_exacta'
            
            elif valor in ['BACHILLERATO DIGITAL']:
                return 'bachillerato_digital'
            
            elif valor in ['BACHILLERATO_PILARES']:
                return 'bachillerato_pilares'
            
            elif valor in ['BECARIA', 'BECARIO']:
                return 'becario/a'
            
            elif valor in ['BECARIA -FORMATO FEBRERO', 'BECARIO -FORMATO FEBRERO']:
                return 'becario/a_formato_febrero'
            
            elif valor in ['BECARIA -FORMATO MARZO', 'BECARIA -FORMATO MARZO']:
                return 'becario/a_formato_marzo'
            
            elif valor in ['BECARIA/TRABAJO COMUNITARIO']:
                return 'becaria_trabajo_comunitario'
            
            elif valor in ['ASESORIA PREPA ABIERTA']:
                return 'asesoria_prepa_abierta'
            
            elif valor in ['ASESORIA PREPA EN LINEA', 'ASESORÍA PREPA EN LINEA', 'ASESORIA PREPA EN LINEA SEP']:
                return 'asesoria_prepa_en_linea'
            
            elif valor in ['ASESORIA PREPARATORIA']:
                return 'asesoria_preparatoria'
            
            elif valor in ['ASESORIA SECUNDARIA', 'ASESORÍA SECUNDARIA', 'ASESORIAS SECUNDARIA','ASESORÍAS SECUNDARIA']:
                return 'asesoria_secundaria_no_especificado'
            
            elif valor in ['ASESORIA SECUNDARIA INEA', 'ASESORÍAS SECUNDARIA INEA']:
                return 'asesoria_secundaria_inea'
            
            elif valor in ['ASESORIA SECUNDARIA INGLÉS']:
                return 'asesoria_secundaria_ingles'
            
            elif valor in ['ASESORIA UNIVERSIDAD']:
                return 'asesoria_universidad'
            
            elif valor in ['ASESORIAS BACHILLERATO CALCUÑO DIFERENCIAL']:
                return 'asesorias_bachillerato_calculo_diferencial'
            
            elif valor in ['ASESORIAS INEA', 'ASESORÍAS INEA', 'ASESORIAS/INEA']:
                return 'asesorias_inea_sin_especificar'
            
            elif valor in ['ASESORIAS INEA SECUNDARIA', 'ASESPROA INEA SECUNDARIA']:
                return 'asesoria_inea_secundaria'
            
            elif valor in ['ASESORIA INEA PRIMARIA']:
                return 'asesoria_inea_primaria'
            
            elif valor in ['ASESORIAS OTROS BACHILLERATOS']:
                return 'asesoria_otros_bachillerato'
            
            elif valor in ['APOYO ADMINISTRATIVO']:
                return 'apoyo_administrativo'
            
            elif valor in ['ASESORIA ADMINISTRACION Y CONTABILIDAD']:
                return 'asesoria_administracion_contabilidad'
            
            elif valor in ['ASESORIA', 'ASESORIA PRESENCIAL', 'ASESORIAS']:
                return 'asesoria'
            
            elif valor in ['ASESORIA/BECARIA', 'ASESORIA/BECARIO', 'ASESORÍAS BECARIO', 'ASESORIAS/BECARIA',
                           'ASESORIAS/BECARIO', 'BECARIA/ASESORIAS', 'BECARIO/ASESORIAS', 'ASESORIAS/BECARIO']:
                return 'asesoria_becarios'
            
            elif valor in ['ASESORIAS/EXACER']:
                return 'asesorias_exacer'
            
            elif valor in ['MATEMATICAS', 'MATEMÁTICAS']:
                return 'matematicas'
            
            elif valor in ['MATEMÁTICAS SECUNDARIA']:
                return 'matematicas_basicas'
            
            elif valor in ['MATEMÁTICAS BÁSICA']:
                return 'matematicas_basicas'
            
            elif valor in ['MI BECA PARA EMPEZAR']:
                return 'mi_beca_para_empezar'
            
            elif valor in ['MIS EMOCIONES EN CORTO']:
                return 'mis_emociones_en_corto'
            
            elif valor in ['MIS PRIMEROS PASOS EN COMPUTACIÓN 2']:
                return 'mis_primeros_pasos_en_computacion_2'
            
            elif valor in ['BECARIO/TRABAJO COMUNITARIO']:
                return 'becario/trabajo comunitario'
            
            elif valor in ['CARPINTERIA']:
                return 'carpinteria'
            
            elif valor in ['CARTONERIA']:
                return 'cartoneria'
            
            elif valor in ['COMIPEMS']:
                return 'comipems'
            
            elif valor in ['COMIPEMS -BIOLOGIA', 'COMIPEMS-BIOLOGIA']:
                return 'comipems_biologia'
            
            elif valor in ['COMIPEMS -MATEMÁTICAS']:
                return 'comipems_matematicas'
            
            elif valor in ['COMIPEMS-CIVICA Y ÉTICA', 'COMIPEMS-FORMACION CÍVICA Y ÉTICA']:
                return 'comipems_civica_etica'
            
            elif valor in ['COMIPEMS-ESPAÑOL']:
                return 'comipems_español'
            
            elif valor in ['COMIPEMS-FISICA', 'FISICA COMIPEMS']:
                return 'comipems-fisica'
            
            elif valor in ['COMIPEMS-GEOGRAFÍA']:
                return 'comipems_geografia'
            
            elif valor in ['COMIPEMS-HABILIDADES MATEMÁTICAS']:
                return 'comipems_habilidades_matematicas'
            
            elif valor in ['COMIPEMS-HISTORIA']:
                return 'comipems_historia'
            
            elif valor in ['COMIPEMS-LINEA']:
                return 'comipems_linea'
            
            elif valor in ['COMIPEMS-QUIMICA']:
                return 'comipems_quimica'
            
            elif valor in ['COMO CREAR TU PAGINA WEB']:
                return 'como_crear_tu_pagina_web'
            
            elif valor in ['COMO CREAR TU TIENDA EN FACEBOOK']:
                return 'como_crear_tu_tienda_en_facebook'
            
            elif valor in ['COMPUTACION', 'COMPUTO', 'COMPUTACIÓN', 'COMPUTACIÓN.', 'INFORMES / USO DE COMPUTO']:
                return 'computacion'
            
            elif valor in ['COMPUTACION BASICA']:
                return 'computacion_basica'
            
            elif valor in ['COMPUTACION EXCEL']:
                return 'computacion_excel'
            
            elif valor in ['INSCRIPCION COMPUTACION', 'INSCRIPCION COMPUTACION']:
                return 'inscripcion_computacion'
            
            elif valor in ['INSCRIPCION COMPUTACION BASICA']:
                return 'inscripcion_computacion_basica'
            
            elif valor in ['INSCRIPCION GUITARRA']:
                return 'inscripcion_guitarra'
            
            elif valor in ['INSCRIPCION A SISTEMAS WEB']:
                return 'inscripcion_a_sistemas_web'
            
            elif valor in ['INSCRIPCION INGLES 7-9']:
                return 'inscripcion_ingles_7_a_9'
            
            elif valor in ['INSCRIPCION INGLES 10 - 13']:
                return 'inscripcion_ingles_10_a_13'
            
            elif valor in ['INSCRIPCION INGLES ADULTOS']:
                return 'inscripcion_ingles_adultos'
            
            elif valor in ['INSCRIPCION A LA ROBOTICA']:
                return 'inscripcion_a_robotica'
            
            elif valor in ['INTRODUCCIÓN AL ALGEBRA', 'INTRODUCIÓN AL ALGEBRA']:
                return 'introduccion al algebra'
            
            elif valor in ['JAPONES']:
                return 'japones'
            
            elif valor in ['JAPONÉS BÁSICO']:
                return 'japones_basico'
            
            elif valor in ['JAPONÉS BASICO I A', 'JAPONÉS BÁSICO I-A']:
                return 'japones_basico_I_a'
            
            elif valor in ['JAPONÉS BASICO I']:
                return 'japones_basico_I'
            
            elif valor in ['JAPONÉS BÁSICO II']:
                return 'japones_basico_II'
            
            elif valor in ['JAPONÉS BASICO I B', 'JAPONÉS BÁSICO I-B']:
                return 'japones_basico_I_b'
            
            elif valor in ['JAPONÉS BÁSICO I A B']:
                return 'japones_basico_I_a_b'
            
            elif valor in ['JAPONÉS BÁSICO II-A']:
                return 'japones_basico_II_a'
            
            elif valor in ['JAPONÉS BÁSICO II-B']:
                return 'japones_basico_II_b'
            
            elif valor in ['TALLER DE INGLES NOCTURNO', 'TALLER DE INGLÉS NOCTURNO']:
                return 'taller_de_ingles_nocturno'
            
            elif valor in ['TALLER DE INGLES NOCTURNO 1']:
                return 'taller_de_ingles_nocturno_1'
            
            elif valor in ['TALLER DE INGLES NOCTURNO 2', 'TALLER DE INGLÉS NOCTURNO 2']:
                return 'taller_de_ingles_nocturno_2'
            
            elif valor in ['OFIMATICA', 'OFIMÁTICA']:
                return 'ofimatica'
            
            elif valor in ['CURSO OFIMÁTICA']:
                return 'curso_ofimatica'
            
            elif valor in ['CURSO OFIMÁTICA 2']:
                return 'curso_ofimatica_2'
            
            elif valor in ['ESCUELA DE CODIGO - INTENSIVO SABADO']:
                return 'escuela_de_codigo_intensivo_sabado'
            
            elif valor in ['ESCUELA DE CÓDIGO PARA MUJERES Y TODOS']:
                return 'escuela_de_codigo_para_mujeres_y_todos'
            
            elif valor in ['USO DE COMPUTADORA', 'USO DE COMPUTADORAS', 'USO DE COMPUTO']:
                return 'uso_de_computadora'
            
            elif valor in ['TALLER DE AJEDREZ']:
                return 'taller_de_ajedrez'
            
            elif valor in ['TALLER DE ÁLGEBRA', 'TALLER DE ALJEBRA']:
                return 'taller_de_algebra'
            
            elif valor in ['MATEMATICAS BACHILLERATO', 'MATEMÁTICAS BACHILLERATO']:
                return 'matematicas_bachillerato'
            
            elif valor in ['MATEMATICAS - CIENCIA']:
                return 'matematicas_ciencia'
            
            elif valor in ['MATEMÁTICAS EXACER']:
                return 'matematicas_exacer'
            
            elif valor in ['MATEMATICAS INEA']:
                return 'matematicas inea'
            
            elif valor in ['MATEMÁTICAS LÚDICAS']:
                return 'matematicas_ludicas'
            
            elif valor in ['MATEMATICAS PRIMARIA', 'MATEMÁTICAS PRÍMARIA']:
                return 'matematicas_primaria'
            
            elif valor in ['MATEMATICAS (NOMBRE DE LA ASESORÍA)']:
                return 'matematicas_sin_nombre_de_asesoria'
            
            elif valor in ['MATEMATICAS PRIMARIA ALTA']:
                return 'matematicas_primaria_alta'
            
            elif valor in ['APOYO BACHILLERATO EXACER']:
                return 'apoyo_bachillerato_exacer'
            
            elif valor in ['APOYO TAREAS CIENCIAS NATURALES', 'APOYO TAREAS GEOGRAFÍA Y C. NATURALES']:
                return 'apoyo_tareas_ciencias_naturales'
            
            elif valor in ['APOYO EN TAREAS GEOGRAFÍA Y C. NATURALES']:
                return 'apoyo_en_tareas_geografia'
            
            elif valor in ['ASESORIAS']:
                return 'asesorias'
            
            elif valor in ['ASESORIAS CIENCIAS NATURALES', 'ASESORÍAS CIENCIAS NATURALES']:
                return 'asesorias_ciencias_naturales'
            
            elif valor in ['ASESORIAS CIENCIAS NATURALES (SECUNDARIA)']:
                return 'asesorias_ciencias_natuales_secundaria'
            
            elif valor in ['ASESORIAS COMPUTACIÓN', 'ASESORIAS-COMPUTACIÓN']:
                return 'asesorias_computacion'
            
            elif valor in ['ASESORÍAS INGRESO LICENCIATURA']:
                return 'asesorias_ingreso_licenciatura'
            
            elif valor in ['ASESORIAS PRIMARA']:
                return 'asesorias_primaria'
            
            elif valor in ['ASESORÍAS PREPA ABIERTA']:
                return 'asesorias_prepa_abierta'
            
            elif valor in ['ASESORIAS PREPA EN LINEA SEP']:
                return 'asesorias_prepa_en_linea_sep'
            
            elif valor in ['ASESORIAS PREPARATORIA']:
                return 'asesorias_preparatoria'
            
            elif valor in ['ASESORÍA GUIA IPN EXAMEN A LICENCIATURA']:
                return 'asesoria_guia_ipn_examen_a_licenciatura'
            
            elif valor in ['ASESORÍAS BACHILLERATO PILARES', 'ASESORÍAS BP']:
                return 'asesorias_bachillerato_pilares'
            
            elif valor in ['ASESORIAS EN PREPA ABIERTA']:
                return 'asesorias_en_prepa_abierta'
            
            elif valor in ['ASESORÍAS INEA-LA PALABRA']:
                return 'asesorias_inea_la_palabra'
            
            elif valor in ['ASESORÍAS INEA-MATEMÁTICAS PARA EMPEZAR']:
                return 'asesorias_inea_matematicas_para_empezar'
            
            elif valor in ['ASESORÍAS INEA-PEC']:
                return 'asesorias_inea_pec'
            
            elif valor in ['ASESORÍAS IPN, ESCOLARIZADO']:
                return 'asesorias_ipn_escolarizado'
            
            elif valor in ['ASESORÍAS LICENCIATURA']:
                return 'asesorias_licenciatura'
            
            elif valor in ['3RO SECUNDARIA']:
                return 'tercero_secundaria'
            
            elif valor in ['prepa abierta', 'PREPA ABIERTA', 'PREPA ABIERTA/USO DE COMPUTO']:
                return 'prepa_abierta'
            
            elif valor in ['PREPA EN LINEA', 'PREPA EN LÍNEA', 'PREPA EN LINEA SEP', 'PREPARATORIA EN LÍNEA']:
                return 'prepa_en_linea'
            
            elif valor in ['CIENCIA Y GEOGRAFÍA', 'GEOGRAFÍA']:
                return 'ciencia_y_geografia'
            
            elif valor in ['INGLES ADULTOS 1']:
                return 'ingles_adultos_1'
            
            elif valor in ['INGLES ADULTOS 6']:
                return 'ingles_adultos_6'
            
            elif valor in ['INGLES APRENDE A CONTAR 9-14 AÑOS']:
                return 'ingles_aprende_a_contar_9_14'
            
            elif valor in ['INGLES APRENDE A CONTAR 15+']:
                return 'ingles_aprende_a_contar_15+'
            
            elif valor in ['INGLÉS BACHILLERATO']:
                return 'ingles_bachillerato'
            
            elif valor in ['INGLES 65+']:
                return 'ingles_65_+'
            
            elif valor in ['INGLES 70+']:
                return 'ingles_70_+'
            
            elif valor in ['INGLÉS BÁSICO II']:
                return 'ingles_basico_2'
            
            elif valor in ['INGLÉS HIBRIDO 25+']:
                return 'ingles_hibrido_25_+'
            
            elif valor in ['INGLES JULIO 10-14']:
                return 'ingles_julio_10_a_14'
            
            elif valor in ['INGLES LINEA 10-14']:
                return 'ingles_linea_10_a_14'
            
            elif valor in ['INGLÉS INFORMES']:
                return 'ingles_informes'
            
            elif valor in ['INGLES NIÑOS 1']:
                return 'ingles_niños_1'
            
            elif valor in ['INGLÉS PRESENCIAL SECUNDARIA']:
                return 'ingles_presencial_secundaria'
            
            elif valor in ['INGLÉS PRESENCIAL SEP-DIC']:
                return 'ingles_presencial_septiempre_diciembre'
            
            elif valor in ['INGRESO A LICENCIATURA']:
                return 'ingreso_a_licenciatura'
            
            elif valor in ['PORTUGUES']:
                return 'portugues'
            
            elif valor in ['PORTUGUÉS BÁSICO 1']:
                return 'portugues_basico_1'
            
            elif valor in ['PORTUGUÉS BÁSICO 2', 'PORTUGUÉS BÁSICO II']:
                return 'portugues_basico_2'
            
            elif valor in ['PORTUGUÉS BÁSICO I A', 'PORTUGUÉS BÁSICO I-A', 'PORTUGUÉS BÁSICO I-AB']:
                return 'portugues_basico_IA'
            
            elif valor in ['PORTUGUÉS BÁSICO I-B', 'PORTUGUÉS BÁSICO I-AB']:
                return 'portugues_basico_IA'
            
            elif valor in ['REGULARIZACIÓN ALGEBRA']:
                return 'regularizacion_algebra'
            
            elif valor in ['PREESCOLAR']:
                return 'preescolar'
            
            elif valor in ['TALLER LENGUAJE Y COMUNICACIÓN', 'TALLER LENGUAJE Y COMUNICACION']:
                return 'taller_lenguaje_y_programacion'
            
            elif valor in ['TALLER LENGUAJE Y COMUNICACIÓN(OYENTE)']:
                return 'taller_lenguaje_y_comunicacion_oyente'
            
            elif valor in ['TALLER EXAMEN LICENCIATURA UNAM-POLI']:
                return 'taller_examen_licenciatura_unam_poli'
            
            elif valor in ['TALLER DE MULTIPLICACIONES']:
                return 'taller_de_multiplicaciones'
            
            elif valor in ['TALLER DE PROGRAMACIÓN']:
                return 'taller_de_programacion'
            
            elif valor in ['TALLER MI PRIMER MAPA', 'TALLER "ELABORANDO MI PRIMER MAPA"']:
                return 'taller_mi_primer_mapa'
            
            elif valor in ['TALLER QUE DIVERTIDO ES APRENDER LAS ESTRUCTURAS NUMÉRICAS ELEMENTALES']:
                return 'taller_aprendiendo_estructuras_numericas_elementales'
            
            elif valor in ['TAI CHI CHUAN', 'TAICHI CHUAN']:
                return 'taichuchuan'
            
            elif valor in ['REGULARIZACION ESPAÑOL', 'REGULARIZACIÓN ESPAÑOL']:
                return 'regularizacion_español'
            
            elif valor in ['REPASO PORTUGUÉS']:
                return 'repaso_portugues'
            
            elif valor in ['ROBOTICA']:
                return 'robotica'
            
            elif valor in ['RÓBOTICA APLICADA']:
                return 'robotica_aplicada'
            
            elif valor in ['ROBÓTICA INTERMEDIO']:
                return 'robotica_intermedio'
            
            elif valor in ['ROBOTICA SCRATCH DE 4 A 5:30', 'SCRATCH']:
                return 'robotica_scratch'
            
            elif valor in ['LA MÁQUINA DE HACER HISTORIAS']:
                return 'la_maquina_de_hacer_historias'
            
            elif valor in ['LÁMPARA AUTOMATIZADA']:
                return 'lampara_automatizada'
            
            elif valor in ['PAGINAS WEB']:
                return 'paginas_web'
            
            elif valor in ['PINTURAS']:
                return 'pinturas'
            
            elif valor in ['PIÑATAS']:
                return 'piñatas'
            
            elif valor in ['PRESENCIAL SEP-DIC']:
                return 'presencial_septiembre_diciembre'
            
            elif valor in ['PRIMARIA']:
                return ['primaria']
            
            elif valor in ['RASTREO DE FOLIO']:
                return 'rastreo_de_folio'
            
            elif valor in ['REGULARIZACIÓN MATEMÁTICAS']:
                return 'regularizacion_matematicas'
            
            elif valor in ['ROBÓTICA: DISPERSADOR DE GEL']:
                return 'robotica_dispersador_de_gel'
            
            elif valor in ['SECUNDARIA']:
                return 'secundaria'
            
            elif valor in ['SECUNDARIA EN LINEA']:
                return 'secundaria_en_linea'
            
            elif valor in ['SECUNDARIA INEA']:
                return 'secundaria_inea'
            
            elif valor in ['TALLER ¿SOY RESILENTE?']:
                return 'taller_soy_resilente'
            
            elif valor in ['TALLER "ELABORANDO MI PRIMER MAPA"']:
                return 'taller_elaborando_mi_primer_mapa'
            
            elif valor in ['TALLER "SISTEMA DE ECUACIONES DE 2X2"']:
                return 'taller_sistema_de_ecuaciones_2x2'
            
            elif valor in ['TALLER DE CARPINTERIA']:
                return 'taller_de_carpinteria'
            
            elif valor in ['TALLER DE COMPUTO. EJE 1.']:
                return 'taller_de_computo_eje_1'
            
            elif valor in ['TALLER DE DIBUJO TECNICO']:
                return 'taller_de_dibujo_tecnico'
            
            elif valor in ['TALLER DE EJERCICIOS IPN']:
                return 'taller_de_ejercicios_ipn'
            
            elif valor in ['TALLER DE FRACCIONES']:
                return 'taller_de_fracciones'
            
            elif valor in ['TALLER DE INGLÉS BÁSICO']:
                return 'taller_de_ingles_basico'
            
            elif valor in ['TRIGONOMETRÍA']:
                return 'trigonometria'
            
            elif valor in ['TRABAJO COMUNITARIO', 'TRABAJO PRPOUESTA COMUNITARIA', 'SERVICIO COMUNITARIO']:
                return 'trabajo_comunitario'
            
            elif valor in ['TRAMITES']:
                return 'tramites'
            
            elif valor in ['VERANO DIVERTIDO MATEMÁTICAS(SEP)']:
                return 'verano_divertido_matematicas_sep'
            
            else:
                return 'unknown'
        
        df_26_hoja['TALLER'] = df_26_hoja['TALLER'].apply(taller_limpio)
        
        def alcaldias(valor):
            if pd.isna(valor):
                return 'desconocido'
            
            valor = str(valor).strip().upper()
            
            if valor in ['VENUSIANO CARRANZA', 'VENUSTIANO C', 'VENUSTIANO CARRANZA']:
                return 'venustiano_carranza'
            
            elif valor in ['IZTAPALAP', 'IZTAPALAPA', 'IZTAPALAPÁ', 'IZTAPALAPA']:
                return 'iztapalapa'
            
            elif valor in ['GUSTAVO A MADERO', 'GUSTAVO A, MADERO', 'GUSTAVO A. MADERO', 'GUSTAVO. A. MADERO',
                           'G. A. M', 'G.A.M', 'GAM', 'GAM0']:
                return 'gustavo_a_madero'
            
            elif valor in ['ALVARO OBREGON', 'ALVARO OBREGÓN', 'ÁLVARO OBREGON', 'Álvaro Obregón']:
                return 'alvaro_obregon'
            
            elif valor in ['BENITO JUAREZ', 'BENITO JUÁREZ']:
                return 'benito_juarez'
            
            elif valor in ['LA MAGDALENA CONTRERAS', 'MAGADANELA CONTRETAS', 'MAGDALENA CONTRERAS']:
                return 'la_magdalena_contreras'
            
            elif valor in ['TLAGUAC', 'TLAHUAC', 'TLÁHUAC', 'TLÀHUAC', 'TLAHUAC SEC. ABIERTA', 
                           'TLAHUC', 'TLHAHUAC', 'TLÁUAC', 'TLHAHUAC', 'TLHUAC']:
                return 'tlahuac'
            
            elif valor in ['CUAHTEMOC', 'CUAHUTEMOC', 'CUAHUTÉMOC', 'CUAUHTECOM', 'CUAUHTÉMOC']:
                return 'cuahutemoc'
            
            elif valor in ['COYOACAN', 'COYOACÁN']:
                return 'coyoacan'
            
            elif valor in ['CUAJIMALPA', 'CUAJIMALPA DE MORELOS']:
                return 'cuajimalpa'
            
            elif valor in ['AZCAPOTZALCO']:
                return 'azcapotzalco'
            
            elif valor in ['XOCHIMILCO']:
                return 'xochimilco'
            
            elif valor in ['TLALPAN', 'TLANPAN', 'TLAPAN']:
                return 'tlalpan'
            
            elif valor in ['IZTACALCO']:
                return 'iztacalco'
            
            else:
                return 'estado_de_mexico_y_colonias_de_la_cdmx'
        
        df_26_hoja['DELEGACIÓN'] = df_26_hoja['DELEGACIÓN'].apply(alcaldias)
        
        df_26_hoja['EDAD'] = pd.to_numeric(df_26_hoja['EDAD'], errors='coerce')
        
        mean_edad = df_26_hoja['EDAD'].mean()
        df_26_hoja['EDAD'] = df_26_hoja['EDAD'].fillna(mean_edad)
        
        df_26_hoja.to_csv(limpios, index=False, encoding='utf-8-sig')
        
        return True
    
    except Exception as e:
        print(f"error en el proceso etl {e}")
        return False

if __name__ == '__main__':
    etl_nopa_2(df_26_hoja, limpios)