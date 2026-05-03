print("hola mundo")

print("proceso etl")

import pandas as pd
import csv 
import logging 
import numpy as np

datos = r"C:\Users\zabu\Desktop\pilaresnopa\pilaresnopa.xlsx"
limpios = r"C:\Users\zabu\Desktop\pilaresnopa\pilaresnopa_limpio.csv"


df_primera_hoja = pd.read_excel(datos, sheet_name=1, header=0)

print(df_primera_hoja.head())

print("la informacion de este documento es:", df_primera_hoja.info())

print("el tipo de dato de la columna edad es:", df_primera_hoja['EDAD'].dtype)
print("el tipo de dato de la columna apellido_p es:", df_primera_hoja['APELLIDO_P'].dtype)
print("el tipo de dato de la columna apellido_m es:", df_primera_hoja['APELLIDO_M'].dtype)
print("el tipo de dato de la columna nombre es:", df_primera_hoja['NOMBRE'].dtype)
print("el tipo de dato de la columna nivel academico es:", df_primera_hoja['NIVEL_ACADEMICO'].dtype)
print("el tipo de dato de la columna estatus es:", df_primera_hoja['ESTATUS'].dtype)
print("el tipo de dato de la columna taller es:", df_primera_hoja['TALLER'].dtype)
print("el tipo de dato de la columna direccion es:", df_primera_hoja['DIRECCION'].dtype)
print("el tipo de dato de la columna delegación es:", df_primera_hoja['DELEGACION'].dtype)
print("el tipo de dato de la columna codigo postal es:", df_primera_hoja['CODIGO_POSTAL'].dtype)
print("el tipo de dato de la columna correo es:", df_primera_hoja['CORREO'].dtype)
print("el tipo de dato de la columna telefono es:", df_primera_hoja['TELEFONO'].dtype)
print("el tipo de dato de la columna folio es:", df_primera_hoja['FOLIO'].dtype)
print("el tipo de dato de la columna realizado es:", df_primera_hoja['REALIZADO'].dtype)

def pipeline_nopa(datos, limpios): 

    try:
        #identificamos valores faltantes
        miss_apellido_p = df_primera_hoja['APELLIDO_P'].isnull().sum()
        if miss_apellido_p > 0: 
            logging.warning(f"faltan {miss_apellido_p} de datos en la columna apellido paterno")

        miss_apellido_m = df_primera_hoja['APELLIDO_M'].isnull().sum()
        if miss_apellido_m > 0: 
            logging.warning(f"faltan {miss_apellido_m} de datos en la columna apellido materno")
        
        miss_nombre = df_primera_hoja['NOMBRE'].isnull().sum()
        if miss_nombre > 0: 
           logging.warning(f"faltan {miss_nombre} de datos en la columna nombre")
        
        miss_sexo = df_primera_hoja['SEXO'].isnull().sum()
        if miss_sexo > 0: 
           logging.warning(f"faltan {miss_sexo} de datos en la columna sexo")
        
        miss_edad = df_primera_hoja['EDAD'].isnull().sum()
        if miss_edad > 0: 
            logging.warning(f"faltan {miss_edad} de datos en la columna edad")
        
        miss_nivel_academico = df_primera_hoja['NIVEL_ACADEMICO'].isnull().sum()
        if miss_nivel_academico > 0: 
            logging.warning(f"faltan {miss_nivel_academico} de datos en la columna nivel academico")
        
        miss_status = df_primera_hoja['ESTATUS'].isnull().sum()
        if miss_status > 0: 
            logging.warning(f"faltan {miss_status} de datos en la columna status")

        miss_taller = df_primera_hoja['TALLER'].isnull().sum()
        if miss_taller > 0: 
            logging.warning(f"faltan {miss_taller} de datos en la columna taller")
        
        missd_direccion = df_primera_hoja['DIRECCION'].isnull().sum()
        if missd_direccion > 0: 
            logging.warning(f"faltan {missd_direccion} de datos en la columna direccion")
        
        miss_delegacion = df_primera_hoja['DELEGACION'].isnull().sum()
        if miss_delegacion > 0: 
            logging.warning(f"faltan {miss_nivel_academico} de datos en la columna nivel academico")

        miss_codigo_postal = df_primera_hoja['CODIGO_POSTAL'].isnull().sum()
        if miss_codigo_postal > 0: 
            logging.warning(f"faltan {miss_codigo_postal} de datos en la columna codigo postal")
        
        miss_correo = df_primera_hoja['CORREO'].isnull().sum()
        if miss_correo > 0: 
            logging.warning(f"faltan {miss_correo} de datos en la columna correo")
        
        miss_telefono = df_primera_hoja['TELEFONO'].isnull().sum()
        if miss_telefono > 0: 
            logging.warning(f"faltan {miss_telefono} de datos en la columna telefono")
        
        miss_folio = df_primera_hoja['FOLIO'].isnull().sum()
        if miss_folio > 0: 
            logging.warning(f"faltan {miss_folio} de datos en la columna folio")
        
        miss_realizado = df_primera_hoja['REALIZADO'].isnull().sum()
        if miss_realizado > 0: 
            logging.warning(f"faltan {miss_realizado} de datos en la columna realizado")

        #segun los datos, en la columna edad, tenemos que nos faltan 1010, si rellenamos con la media

        #algunos estan con NA 

        # Convertir EDAD a número (int o float)

        df_primera_hoja['EDAD'] = pd.to_numeric(df_primera_hoja['EDAD'], errors='coerce')

        mean_edad = df_primera_hoja['EDAD'].mean()

        df_primera_hoja['EDAD'] = df_primera_hoja['EDAD'].fillna(mean_edad)

        #convertimos para las siguientes columnas igual de object a string

        df_primera_hoja['APELLIDO_P'] = df_primera_hoja['APELLIDO_P'].astype('string')
        df_primera_hoja['APELLIDO_M'] = df_primera_hoja['APELLIDO_M'].astype('string')
        df_primera_hoja['NOMBRE'] = df_primera_hoja['NOMBRE'].astype('string')

        def inferir_nivel_academico(nivel):
            if pd.isna(nivel):
                return 'unknown'
            
            nivel = str(nivel).strip().upper()

            if nivel in  ['1 KINDER']:
                return 'primero_kinder'
            elif nivel in ['1 PRIMARIA', '1RO PRIMARIA', '1RO PRIMARIA EN CURSO']:
                return 'primer_primaria'
            elif nivel in ['2 DO PRIMARIA', '2DO PRIMARIA', '2DO. DE PRIMARIA', '2DO PRIMARIA',
                           'PRIMARIA 2DO']:
                return 'segundo_primaria'
            elif nivel in ['3 PRIMARIA', '3ERO PRIMARIA', '3RO PRIMARIA', '3RO RPIMARIA', '3RON PRIMARIA',
                           'PRIMARIA 3', 'PRIMARIA 3RO', ]:
                return 'tercero_primaria'
            elif nivel in ['4 PRIMARIA', '4TO PRIMARIA', '4 TO PRIMARIA', 'PRIMARIA 4TO']:
                return 'cuarto_primaria'
            elif nivel in ['5 PRIMARIA', '5TO PRIMARIA', '5TO. PRIMARIA', 'PRIMARIA 5']:
                return 'quinto_primaria'
            elif nivel in ['6TO PRIMARIA', '6TO DE PRIMARIA', 'PRIMARIA 6', 'PRIMARIA 6 DO']:
                return 'sexto_primaria'
            elif nivel in ['PRIMARA', 'PRIMARIA', 'PRIMERIA']:
                return 'primaria'
            elif nivel in ['1 SECUNDARIA', '1RO SECUNDARIA', '1RTO SECUNDARIA']:
                return 'primero_secundaria'
            elif nivel in ['2DO SECUNDARIA', 'SECUNDARIA 2', 'SECUNDARIA 2DO']:
                return 'segundo_secundaria'
            elif nivel in ['3RO SEC', '3ERO. SECUNDARIA', '3RO SECUNDARIA', 'SECUNDARIA 3']:
                return 'tercer_secundaria'
            elif nivel in ['ECUNDARIA', 'SD', 'SECUNDARIA', 'Secundaria', 'SECUNDARIA', 'SECUNDARIAS',
                           'SECUNDRIA', 'SECUNDSRIA']:
                return 'secundaria'
            elif nivel in ['SIN ESTUDIOS', 'SIN ESTUDIO']: 
                return 'sin_estudios'
            elif nivel in ['TECNICO', 'TÉCNICA', 'TECNICA', 'TECNICO PROFESIONAL', 'C. TECNICA', 'CARRERA TECNICA', 
                           'BACHILLERATO TECNICO', ]:
                return 'tecnico'
            elif nivel in ['PREPARATORIA', 'PREPA', 'PREPARATOIA', 'PREPARATPRIA', 'BACHILERATO', 'BACHILLERATO', 'BACHILLERES',
                           'BACHILLERATO PILARES']:
                return 'media_superior'
            elif nivel in ['UNIVERCIDAD', 'UNIVERSIDAD']:
                return 'superior'
            elif nivel in ['LICENCIARURA', 'LICENCIATURA', 'LICENCITURA', 'LICEN']:
                return 'licenciatura'
            elif nivel in ['C. COMERCIAL', 'COMERCIAL', 'COMERCIO', 'CARRERA COMERCIAL']:
                return 'carrerca_comercial'
            elif nivel in ['PREPRIMARIA', 'PRESCOLAR', 'PREESCOLAR', 'KINDER']:
                return 'prescolar'
            elif nivel in ['INDEFINIDO', 'NINGUNO', 'SIN', 'SIN ALFABETIZACION', 'SIN DATO',
                           'PERSONAS DISCAPACIDAD SEVERA', 'ESTEBAN']: 
                return 'sin_dato_alguno'
            elif nivel in ['PREPA EN LINEA', 'PREPA EN LINEA SEP']:
                return 'prepa_en_linea'
            else:
                return 'otro_grado'
        
        df_primera_hoja['NIVEL_ACADEMICO'] = df_primera_hoja['NIVEL_ACADEMICO'].apply(inferir_nivel_academico)

        def normalizar_sexo(valor): 
            if pd.isna(valor):
                return 'desconocido'
            
            valor = str(valor).strip().upper()

            if valor in ['MASCULINO', 'HOMBRE', 'HOMBRES', 'NOMBRE', 'HOMBRE',
                         'HOM,BRE', 'H', 'hombre'
                         ]:
                return 'Hombre'
            elif valor in ['MUJER', 'MIJER', 'MJUJER', 'MLUJER', 'MUJE5R', 'MUJER']:
                return 'Mujer'
            else: 
                return 'Desconocido'
            
        df_primera_hoja['SEXO'] = df_primera_hoja['SEXO'].apply(normalizar_sexo)

        #para las actividades 

        def actividades(valor):
            if pd.isna(valor):
                return 'desconocido'
            
            valor = str(valor).strip().upper()

            if valor in ['ASESORIA ACADEMIA MATEMATICA', 'ASESORIA MATEMATICAS', 'ASESORIA MATEMÁTICA',
                         'ASESORÍA MATEMÁTICAS', 'asesoria mateticas', 'ASESORIAS-MATEMATICAS', 
                         'ASESORIA-MATEMÁTICAS', 'ASESORIA/MATEMATICAS','ASESORIA/MATEMÁTICAS',
                         'ASESORIA-METEMÁTICAS', 'ASESORIAS MATEMÁTICAS', 'ASESORIAS/MATEMATICAS',
                         ]:
                return 'asesoria_matematicas'
            
            elif valor in ['ASESORIA ACADEMIA', 'ASESORIA ACADÉMIA']:
                return 'asesoria_academia'
            
            elif valor in ['CIBER ESUELA', 'CIBERESCUELA']:
                return 'ciberescuela'
            
            elif valor in ['ECOEMS / BIOLOGIA', 'ECOEMS/BIOLOGIA', 'COMIPEMS / BIOLOGIA', 'INGRESO A BACHILLERATO BIOLOGIA',
                           'INGRESO BACHILLERATO/BIOLOGIA', '']:
                return 'ecoems_biologia'
            
            elif valor in ['COMIPEMS / FISICA', 'COMIPEMS/FISICA', 'ECOEMS / FISICA', 'ECOEMS / FISICA']:
                return 'ecoems_fisica'
            
            elif valor in ['COMIPEMS / QUIMICA', 'ECOEMS/QUIMICA']:
                return 'ecoems_quimica'
            
            elif valor in ['COMIPEMS/GEOGRAFIA', 'ECOEMS/GEOGRAFIA', 'INGRESO BACHILLERATO/GEOGRAFIA']:
                return 'ecoems_geografia'
            
            elif valor in ['EXAMEN UNICO/ALGEBRA', 'EXAMEN ÚNICO/ALGEBRA']:
                return 'examen_unico_algebra'
            
            elif valor in ['EXAMEN UNICO/BIOLOGIA', 'EXAMEN  UNICO/BIOLOGIA']:
                return 'examen_unico_biologia'

            elif valor in ['JAPONES', 'JAPONÉS', 'JAPÓNES', 'JAPONES *']:
                return 'japones'
            
            elif valor in ['MATEMATICAS SEC', 'MATEMATICAS SECUNDARIA', 'MATEMÁTICAS SECUNDARIA', 'MATEMATICAS/SECU',
                           'MATEMATICAS/SECUNDARIA']:
                return 'matematicas_secundaria'
            
            elif valor in ['COMIPEMS / MATEMATICAS', 'COMIPEMS/MATEMÁTICAS', 'ECOEMS / MATEMATICAS',
                           'ECOEMS/MATEMATICAS', 'ECOEMS/MATEMÁTICAS']:
                return 'ecoems_matematicas'
            
            elif valor in ['EXAMEN ÚNICO/IMATEMATICAS', 'EXAMEN UNICO/MATEMATIC AS', 
                           'EXAMEN UNICO/MATEMATICAS', 'EXAMEN UNICO/MATEMÁTICAS', 'EXAMEN UNICO/matematicas',
                           'EXAMEN UNICO/TRIGONOMETRICA', 'EXMEN ÚNICO/MATEMATICAS', 'EXMEN ÚNICO/MATEMÁTICAS', 
                           'EXMEN UNICO/matematicas', 'EXAMEN UNICO/MATEMATICAS', 'EXAMEN UNICO/MATEMÁTICAS', 'EXAMEN UNICO/matemmaticas', 
                           'EXAMEN UNICO/MATEMATICAS']:
                return 'examen_unico_matematicas'
            
            elif valor in ['EXAMEN UNICO/PROBABILIDAD', 'EXAMEN ÚNICO/PROBABILIDAD']:
                return 'examen_unico_probabilidad'
            
            elif valor in ['EXAMEN UNICO/QUIMICA', 'EXAMEN ÚNICO/QUIMICA']:
                return 'examen_unico_quimica'
            
            elif valor in ['EXAMEN UNICO/REPASO FILOSOFIA', 'EXAMEN ÚNICO/REPASO FILOSOFIA']:
                return 'examen_unico_filosofia'
            
            elif valor in ['EXAMEN ÚNICO/HAB. MATEMÁTICAS', 'EXAMEN UNICO/HABILIDADES MATEMÁTICAS']:
                return 'examen_unico_hab_matematicas'
            
            elif valor in ['APOYO A TAREAS', 'APOYO TAREAS']:
                return 'apoyo_tareas'
            
            elif valor in ['COMIPEMS HAB. MATEMÁTICAS', 'ECOEMS / HABILIDAD', 'ECOEMS / HABILIDAD MATEMATICAS',
                           'ECOEMS HABILIDAD-MATEMÁTICAS', 'ECOEMS/HABILIDAD MATEMATICAS',
                           'ECOEMS/HABILIDADES MATEMÁTICAS', 'EXAMEN UNICOMATEMATICAS', 'EXAMEN UNICO /FUNCIONES',
                           'EXAMEN UNICO ALGEBRA', 'EXAMEN UNICO MODULAR/MATEMATICAS', 'EXAMEN UNICO MODULAR/MATEMÁTICAS',
                           'EXAMEN_UNICO_MATEMATICAS', 'EXAMEN_UNICO_MATEMÁTICAS', 'EXAMEN UNICO-MATEMATICAS',
                           'EXAMEN UNICOñ/HAB. MATEMÁTICA']:
                return 'habilidad_matematicas'
        
            elif valor in ['EXAMEN UNICO/COMPUTACION', 'EXAMEN UNICO/COMPUTO']:
                return 'examen_unico_computo'
            
            elif valor in ['EXAMEN UNICO/ECOLOGIA', 'EXAMEN ÚNICO/ECOLOGIA', 'EXAMEN UNICO/ECOLOGIA     LA NOPALERA']:
                return 'examen_unico_ecologia'
            
            elif valor in ['EXAMEN UNICO/ESPAÑOL', 'EXAMEN ÚNICO/ESPAÑOL']:
                return 'examen_unico_español'
            
            elif valor in ['EXAMEN_UNICO', 'EXAMEN ÚNICO', 'EXAMEN UNICO /', 'EXAMEN UNICO/', 
                           'EXAMEN UNICO/EXAMEN UNICO', 'EXANEB UNICO', 'EXEMEN UNICO', 'EXAMEN UNICO /', '']:
                return 'examen_unico'

            elif valor in ['EXAMEN UNICO/GEOGRAFIA', 'EXAMEN  ÚNICO/GEOGRAFIA','EXAMEN ÚNICO/GEOGRAFIA', 
                           'EXAMEN ÚNICO/GEOGRAFÍA']:
                return 'examen_unico_geografia'
            
            elif valor in ['EXAMEN UNICO/HSITORIA']:
                return 'examen_unico_historia'
            
            elif valor in ['EXAMEN UNICO/informatica', 'EXAMEN UNICO/INFORMATICA', 'EXAMEN ÚNICO/INFORMATICA']:
                return 'examen_unico_informatica'
            
            elif valor in ['TIC', 'TIC´S', 'TIC`S', 'TICS']: 
                return 'tics'
            
            elif valor in ['TALLER PEDAGOGICO', 'TALLER PEDAGÓGICO']:
                return 'taller_pedagogico'
            

            elif valor in ['EXA,MEN ÚNICO/HISTORIA', 'EXAMEN UNICO/HISTORIA', 'EXAMEN UNICO/HISTORIA',
                           'EXAMEN ÚNICO/HISTORIA', 'EXAMEN UNICO/HSITORIA', 'EXEMEN UNICO/HISTORIA', 'EXEMEN UNIC0/HISTORIA',
                           'EXMEN ÚNICO/HISTORIA']:
                return 'examen_unico_historia'
            
            elif valor in ['EXAM UNICO FISICA', 'EXAMEN unico/FISICA', 'EXAMEN UNICO /FISICA',
                           'EXAMEN UNICO/FISICA', 'EXAMEN ÚNICO/FISICA', 'Examen unico/fisica',
                           'EXAMEN UNICO/FISICA', 'EXAMEN ÚNICO/FISICA', 'EXEMEN UNICO/FISICA',
                           'EXEMEN UNICO / FISICA', 'EXAMEN/FISICA']:
                return 'examen_unico_fisica'
            
            elif valor in ['EXAMEN UNICO/HAB. MATEMATICA', 'EXAMEN UNICO/HAB. MATEMÁTICA',
                           'EXAMEN ÚNICO/HAB. MATEMÁTICA', 'EXAMEN UNICO/HAB. MATEMATICAS', 
                           'EXAMEN UNICO/HAB. MATEMÁTICAS, EXAMEN ÚNICO MATEMÁTICAS', 
                           'EXAMEN ÚNICO/HAB.MATEMÁTICAS', 'EXAMEN UNICO/HAB.MATEMÁTICA',
                           'EXAMEN UNICO/HAB. MATEMÁTICA', 'EXAMEN ÚNICO/HAB.MATEMATICA',
                           'EXAMEN UNICO/HAB. MATEMATICAS', 'EXAMEN UNICO/HAB.MATEMÁTICAS', 
                           'EXAMEN UNICO/HABILIDAD MATEMATICA', 'EXAMEN UNICO/HABILIDAD MATEMÁTICA',
                           'EXAMEN UNICO/HABILIDAD MATEMATICA', 'EXAMEN UNICO/HABILIDAD MATEMATICA', 
                           'EXAMEN UNICO/HABILIDAD MATEMÁTICA', 'EXAMEN UNICO/HABILIDAD MATEMÁTICAS',
                           'EXAMEN UNICO/HABILIDADES MATEMATICAS', 'EXAMEN UNICO/HABILIDADES MATEMÁTCIAS',
                           'EXAMEN UNICOñ/HAB.MATEMÁTICAS', 'HAB. MATEMÁTICAS', 'HABILIDAD MATEMATICA',
                           'HABILIDAD MATEMÁTICA', 'HABILIDADES MATEMÁTICAS',  
                           'HABILIADES MATEMATICAS7EXAMEN UNICO', 'CURSO BACHILLERATO/HABILIDAD MATEMATICA']:
                
                return 'examen_unico_habilidades_matematicas'
            
            elif valor in ['COMIPEMS/HISTORIA', 'COMIPEMS/HISTORIA', 'ECOEMS/historia', 'ECOEMS/HISTORIA',
                           'ECOEMS/HISTORIA', 'CURSO BACHILLERATO HISTORIA']: 
                return 'ecoems_historia'
            
            elif valor in ['EXAMEN UNICO/USO DE COMPUTO', 'EXAMEN ÚNICO/USO DE COMPUTO']:
                return 'examen_unico_uso_de_computo'
            
            elif valor in ['FRAN CE', 'FRANCCES', 'FRANCES', 'FRANCÉS', 'FRANCÈS']:
                return 'frances'
            
            elif valor in ['GENERACION DE FOLIO', 'GENERACIÓN DE FOLIO', 'GENERACION FOLIO',
                           'GENERACIONDE FOLIO', 'USO DE COMPUTO/CREACIÓN DE FOLIO', 'CREACIÓN DE FOLIO', 'folio',
                           'FOLIO', 'FOLIO NUEVO', 'FOLIO NUEVO PILARES', 'FOLIO PILARES NUEVO', 'FOLIO PILARES/COMPUTACIÓN']:
                return 'generacion_folio'
            
            elif valor in ['INFORMES ACTIVIDADES', 'INFORME ACTIVIDADES']:
                return 'informe_actividades'
            
            elif valor in ['LECTO-ESCRITURA', 'LECTOESCRITURA', 'LECTROESCRITURA']:
                return 'lecto_escritura'
            
            elif valor in ['USO CELULAR', 'USO DE CELILAR', 'USO DE CELULAR' , 'USO DEL CELULAR']:
                return 'uso_celular'
            
            elif valor in ['COMPUTACION', 'COMPUTACIÓN', 'COMPUTADORA', 'COMPUTO', 'COMPÚTO', 'USO DE COMPUTADORA', 
                           'USO DE COMPUTO', 'USO DE COMPUTO', 'USO DE COMPÚTO', 'USO DE COMPUTOI', 'USO DE EQUIPO DE COMPUTO', 'USON DE COMPUTO', 'Uso pc',
                           'USO COMPUTADORA', 'USO COMPUTO', 'USO DE CO', 'USO DE COMPU', 'uso computadora', 'PREPA ABIERTA/USO DE COMPUTO',
                           'TIC USO DE COMPUTADORA']:
                return 'uso_de_computadora'
            
            elif valor in ['R FOLIO PILARES', 'REC FOLIO', 'REC. DE FOLIO', 'REC. FOLIO', 'RECUÉRACIO DE FOLIO', 
                           'RECUPERACION FOLIO', 'RECUPERACIÓN DE FOLIO', 'RECUPERACIÓN FOLIO', 'RECUPERACION DE FOLIO|',
                           'RECUPERACION DE FOPLIO', 'RECUPERAR FOLIO']:
                return 'recuperar_folio'
            
            elif valor in ['EXAMEN UNICO/ETICA', 'EXAMEN  UNICO/ETICA', 'EXAMEN ÚNICO/ETICA', 'EXAMEN ÚNICO/ETICA       LA NOPALERA']:
                return 'examen_unico_etica'
            
            elif valor in ['EXAMEN UNICO/FILOSOFIA', 'EXAMEN UNICO/FILOFOFIA']: 
                return 'examen_unico_filosofia'
            
            elif valor in ['INGES', 'INGLES', 'INGLES/ROBOTICA/COMPUTACION']:
                return 'ingles'
            
            elif valor in ['INSCRIPCION A CURSO DE VERANO', 'INSCRIPCIÓN A CURSO DE VERNAO']:
                return 'inscripcion_curso_verano'
            
            elif valor in ['MATE PRIMARIA', 'MATEMATICAS PRIMARIA', 'MATEMATICAS primaria', 'matematicas primaria']:
                return 'matematicas_primaria'
            
            elif valor in ['prepa abierta', 'PREPA ABIERTA', 'PREPA ABIERTA/USO DE COMPUTO']:
                return 'prepa_abierta'
            
            elif valor in ['PREPA EN LINEA', 'PREPA EN LÍNEA', 'PREPA EN LINEA SEP']:
                return 'prepa_en_linea'
            
            else: 
                return 'Desconocido'

        df_primera_hoja['TALLER_LIMPIO'] = df_primera_hoja['TALLER'].apply(actividades) 

        #en la columna sexo tenemos que nos faltan 371, estos los rellenamos en funcion del nombre
        #por ejemplo si nombre es edgar, entonces sexo es masculino

        posibles_nombres_masculinos = [
            'ALAN', 'ULISES', 'RODRIGO', 'EDUARDO',
            'CARLOS', 'MARIO', 'CRISTIAN', 'EDGAR',
            'ERNESTO', 'HERNAN', 'CESAR', 'MARIO',
            'DAMIAN', 'PABLO', 'GAEL', 'ANTONIO',
            'GILBERTO', 'LUIS', 'JAVIER', 'JESUS', 
            'OMAR', 'JUAN'
        ]


        posibles_nombres_femeninos = [
            'ALONDRA', 'SUSANA', 'LIDIA', 'KAREN',
            'MARIA', 'ANA', 'SELENE', 'ANGELA', 'MIA',
            'KAREN', 'ITZEL', 'NATALIA', 'REGINA', 'SANDRA',
            'YOLANDA', 'ABRIL', 'MONSERRAT', 'ADRIANA', 'LOURDES',
            'LEILANY', 'LEYLANI', 'DANIELA', 'FERNANDA',
            'WENDY', 'GABRIELA'
        ]

        def alcaldia(nombre): 
            if pd.isna(nombre):
                return 'unknow'
            
            if nombre in ['AZCAPOTZALCO', 'AZCALPOTZALCO02469']:
                return 'azcapotzalco'
            
            elif nombre in ['TLAHUAC', 'TLAHAC', 'TLAHAUAC', 'tlahuac', 'TLAHUAC',
                            'TLÁHUAC', 'TLÀHUAC', 'TLAUAC', 'TLHAHUAC', '']:
                return 'thahuac'
            
            elif nombre in ['IZTAPALAPA']: 
                return 'iztapalapa'
            
            elif nombre in ['XOCHIMILCO']:
                return 'xochimilco'
            
            elif nombre in ['MILPA_ALTA']:
                return 'milpa_alta'
            
            else: 
                return 'desconocido'
            
        df_primera_hoja['DELEGACION'] = df_primera_hoja['DELEGACION'].apply(alcaldia)

        def status(nombre):
            if pd.isna(nombre):
                return 'unknown'
            
            nombre = nombre.upper()

            if nombre in ['6 TO', '6°', '6°TO', '6o', '6to', '6TO', '']:
                return '6to_sin_especificar'

            elif nombre in ['6° SEMESTRE', '6t semestre']:
                return '6to_semestre'

            elif nombre in ['1re GRADO' '1RE GRADO']:
                return 'primer_grado'

            elif nombre in ['1RE SEMESTRE', '1RE SEM']:
                return 'primer_semestre'

            elif nombre in ['1ERO', '1ro', '1RO']:
                return 'primero_sin_especificar'
            
            elif nombre in ['1RO SECUNDARIA']:
                return 'primero_secundaria'

            elif nombre in ['2DO', '2°', '2do', '2DO', '2DO . GRADO', '2ro', '2DO.', '2to']:
                return 'segundo_sin_especificar'
            
            elif nombre in ['2 SEC', '2 SECUNDARIA']:
                return 'segundo_secundaria'
            
            elif nombre in ['2DO PRIMARIA']:
                return 'segundo_primaria'
            
            elif nombre in ['3 PRIMARIA', '3 PRIMERIA']:
                return 'tercero_primaria'

            elif nombre in ['3 RO', '3! GRADO', '3°', '3DO SE', '3ERO', '3ERO', '3o', '3ro', 
            '3ro', '3RO', '3RO.', '3rro']:
                return 'tercero_sin_especificar'

            elif nombre in ['3 SECUNDARIA']:
                return 'tercero_secundaria'

            elif nombre in ['3°KINDER']:
                return 'tercero_kinder'
            
            elif nombre in ['3RE SEMESTRE']:
                return 'tercer_semestre'
            
            elif nombre in ['4', '4 TO', '4°', '4to', '4TO', '4TO SEMESTRE']:
                return 'cuarto_sin_especificar'
 
            elif nombre in ['5', '5 to', '5 TO', '5 TO.', '5°', '5° SEM', '5to', '5TO', '5TO.', '5to.semestre']:
                return 'quinto_sin_especificar'
            
            elif nombre in ['7°']:
                return 'septimo_sin_espcificar'

            elif nombre in ['8 TVO.', '8°', '8vo. semestre']:
                return 'octavo_sin_especificar'
            
            elif nombre in ['9°']:
                return 'noveno_sin_especificar'
            
            elif nombre in ['10°', '10']:
                return 'decimo_sin_especificar'
            
            elif nombre in ['11']:
                return 'onceavo_sin_especificar'

            elif nombre in ['1 RO', '1°', '1E5 SEMESTRE']:
                return 'primero_sin_especificar'
            
        def colonia(nombre): 
            if pd.isna(nombre):
                return 'unknown'

            if nombre in ['LA N OPALERA', 'LA NAOPALERA', 'LA NO´PALERA', 'LA NOPAERA', 'LA NOPALERA', 'la nopalera', 'LA NOPLAERA',
                          'NOPALERA', 'NOPÁLERA']:
                return 'la_nopalera'
            
            elif nombre in ['AGRIC. METROPOLITANA', 'AGRICOLA METROPOLITANA', 'AGRÍCOLA METROPOLITANA', 'AGRICOLA METROPOLITANATLAHUAC',
                          'NETROPOLITANA']:
                return 'agricola_metropolitana'
            
            elif nombre in ['DEL M AR', 'DEL M,AR', 'DEL MAR', ',DEL MAR']:
                return 'del_mar'
            
            elif nombre in ['LOS  OLIVOS', 'LOS OLIVOS', 'LOSOLIVOS', 'OLIVOS']:
                return 'los_olivos'
            
            elif nombre in ['EL MOLINO', 'EL MOLIMO', 'EL MOLINO TEZONCO']:
                return 'el_molino'
            
            elif nombre in ['VILLA CENTRO AMERICANA', 'VILLA CENTROAMERICANA', 'VILLACENTROAMERICANA', 'CENTRO AMERICANA']:
                return 'villa_centro_americana'

            elif nombre in ['ELIPSIS DE AMOR', 'ELIXIR DE AMOR', 'ELIXIS DE AMOR']:
                return 'elipsis_de_amor'

            elif nombre in ['LA CONCHITA', 'LA COCHITA', 'LA CONCHITA ZAPOTITTLAN', '']:
                return 'la_conchita'
            
            elif nombre in ['LA ESTACION', 'LA ESTACIÓN']:
                return 'la_estacion'
            
            elif nombre in ['SANTA ANA', 'SANTA ANA PONIENTE', 'SANTA ANA PTE', 'SNTA ANA PONIENTE', 'STA ANA PONIENTE',
                            'STA. ANA PONIENTE', 'STA ANA PONIENTETLAHUAC',]:
                return 'santa_ana_poniente'
            
            elif nombre in ['LAS ARBOLEDAS', 'LAS AROLEDAS']:
                return 'las_arboledas'
            
            elif nombre in ['SANTIAGO ZAPOTITLAN', 'SANTIAGO ZAPOTITLÁN']:
                return 'santiago_zapotitlan'

            elif nombre in ['ZAPOTITLAN', 'ZAPOTITLA']:
                return 'zapotitlan'
            
            else: 
                return 'unknown'
        
        df_primera_hoja['DIRECCION'] = df_primera_hoja['DIRECCION'].apply(colonia)
            

        def inferir_sexo(nombre):
            if pd.isna(nombre):
                return 'unknown'
            
            nombre = nombre.upper()

            if nombre in posibles_nombres_femeninos:
                return 'FEMENINO'
            elif nombre in posibles_nombres_masculinos: 
                return 'MASCULINO'
            else: 
                return 'unknown'
            
        df_primera_hoja['SEXO_INFERIDO'] = df_primera_hoja['NOMBRE'].apply(inferir_sexo)


        #rellenamos las demas faltantes

        df_primera_hoja['NIVEL_ACADEMICO'] = df_primera_hoja['NIVEL_ACADEMICO'].fillna('sin_nivel_academico')

        df_primera_hoja['APELLIDO_P'] = df_primera_hoja['APELLIDO_P'].fillna('sin_apellido_patero')

        df_primera_hoja['ESTATUS'] = df_primera_hoja['ESTATUS'].fillna('sin_estatus')

        df_primera_hoja['TALLER'] = df_primera_hoja['TALLER'].fillna('sin_taller')

        df_primera_hoja['DIRECCION'] = df_primera_hoja['DIRECCION'].fillna('sin_direccion')

        df_primera_hoja['TELEFONO'] = df_primera_hoja['TELEFONO'].fillna('sin_telefono')

        df_primera_hoja['DELEGACION'] = df_primera_hoja['DELEGACION'].fillna('sin_folio')

        df_primera_hoja['FOLIO'] = df_primera_hoja['FOLIO'].fillna('sin_folio')

        df_primera_hoja['CODIGO_POSTAL'] = df_primera_hoja['CODIGO_POSTAL'].fillna('sin_codigo_postal')

        #guardamos el csv

        df_primera_hoja.to_csv(limpios, index=False, encoding='utf-8-sig')


        return True 

    except Exception as e:
        print(f"Hubo un error en el proceso etl: {e}") 
        return False 

if __name__ == '__main__':
    pipeline_nopa(datos, limpios)
