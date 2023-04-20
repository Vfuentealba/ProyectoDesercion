version_datos = 'E1'

sql =  """
SELECT  
    ANOS_CCOD, 
    INST_TNEMOTECNIA, 
    SEDE_TDESC,
    ZONA_TDESC,
    AREA_TDESC ,
    JORN_TDESC, 
    SEXO_TDESC  ,  
    TCOL_TDESC, 
    CANT_DIAS_MATR, 
    CASE WHEN fiador_alumno = 1 then 'Alumno'
         WHEN AD.pare_ccod in (1,2,9,10) then 'Padres'
         ELSE 'Otros'
    END  PARENTESCO_FIADOR_NEW,    
    CANT_PERIODOS_POSTULACIONES, 
    VECES_ACCESOS_APP,   
    EV_DIAGNOSTICA_2, 
    EV_DIAGNOSTICA_4, 
    CASE WHEN TIENE_BENEFICIO_GCO  = 1 THEN 'G'
         WHEN TIENE_BENEFICIO_GCO  = 2 THEN 'C'
         WHEN TIENE_BENEFICIO_GCO  = 3 THEN 'I'
    ELSE 
        'SB'
    END tipo_beneficio     
    ,
    PROMEDIO_ASISTENCIA
    , 
    MONTO_DEUDA
    ,
    PROMEDIO_NOTAS, 
    DECODE(RESPONDE_ENCUESTA_AN,0,'N','S') RESPONDE_ENCUESTA_AN,
    ROUND(( ASIGNATURAS_CON_RIESGO_NOTAS / 
    DECODE(cantidad_asignaturas_alumno,0,1,cantidad_asignaturas_alumno)) ,1) P_ASIG_RIESGO,    
    LTRIM(RTRIM(codigo_asignatura_mat_alg_ss)) codigo_asignatura_mat_alg_ss,
    ES_DESERTOR
    ,
    PERS_NCORR, EMAT_TDESC,PERS_NRUT, PERS_NRUT||'-'|| DV(PERS_NRUT) RUT_ALUMNO_CDV  
from  alumnos_nuevos_desercion ad,
      inacap.sedes ss,
      inacap.zonas_geograficas zg,
      siga.instituciones ii,
      siga.areas_academicas aa,
      siga.jornadas jo,
      siga.planes_estudio pl,
      siga.estados_matriculas em,
      siga.tipos_alumnos ta,
      siga.sexos sex,
      siga.estados_civiles ec,
      siga.tipos_colegios tc,
      siga.tipos_ensenanza_colegios t1,
      siga.tipos_ensenanza_colegios t2,
      siga.tipos_ensenanza_colegios t3,
      siga.parentescos par ,
      siga.ocupaciones ocu    
where  ad.inst_ccod = ii.inst_ccod(+)
and    ad.sede_ccod = ss.sede_ccod(+)
and    ad.zona_ccod = zg.zona_ccod(+)
and    ad.area_ccod = aa.area_ccod(+)
and    ad.jorn_ccod = jo.jorn_ccod(+)
and    ad.plan_ccod = pl.plan_ccod(+)
and    ad.emat_ccod = em.emat_ccod(+)
and    ad.talu_ccod = ta.talu_ccod(+)
and    ad.sexo_ccod = sex.sexo_ccod(+)
and    ad.eciv_ccod = ec.eciv_ccod(+)
and    ad.tcol_ccod = tc.tcol_ccod(+)
and    ad.tien1_ccod = t1.tien_ccod(+)
and    t1.tien_nnivel (+)= 1
and    ad.tien2_ccod = t2.tien_ccod(+)
and    t2.tien_nnivel (+)= 2
and    ad.tien3_ccod = t3.tien_ccod(+)
and    t3.tien_nnivel (+)= 3
and    ad.pare_ccod  = par.pare_ccod(+)
and    ad.ocup_ccod  = ocu.ocup_ccod(+)
AND   VERSION_DATOS = 'E5'
"""