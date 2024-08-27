from rest_framework.views import APIView
from rest_framework.response import Response
from decimal import Decimal
from rest_framework import status
from ..models import DatosUsuario
from ..serializers import DatosUsuarioSerializer
from .analizadorsalud import AnalizadorSalud

class HealthIndicatorsAPIView(APIView):
    queryset = DatosUsuario.objects.all()
    serializer_class = DatosUsuarioSerializer

    def get(self, request, *args, **kwargs):
        usuario_id = self.kwargs.get('usuario_id')
        try:
            paciente = DatosUsuario.objects.get(user_id=usuario_id, tipo='inicial')  # O 'final' según sea necesario
        except DatosUsuario.DoesNotExist:
            return Response({"detail": "Datos del usuario no encontrados."}, status=status.HTTP_404_NOT_FOUND)
        
        # 1. Peso
        peso_status = AnalizadorSalud.clasificar_peso(paciente.peso)
        
        # 2. Altura
        altura_status = AnalizadorSalud.clasificar_altura(paciente.altura)
        
        # 3. IMC
        imc = AnalizadorSalud.calcular_imc(paciente.peso, paciente.altura)
        imc_status = AnalizadorSalud.clasificar_imc(imc)
        
        # 4. Presión Arterial Sistólica
        sistolica_status = AnalizadorSalud.clasificar_presion_sistolica(paciente.presion_sistolica )
     
       
        
        # 5. Presión Arterial Diastólica
     
        diastolica_status = AnalizadorSalud.clasificar_presion_diastolica(paciente.presion_diastolica)
      
        
        # 6. Radio Abdominal
       
        radio_abdominal_status = AnalizadorSalud.clasificar_radio_abdominal(paciente.radio_abdominal,paciente.sexo)
       
        
        # 7. Grasa Corporal (%)

        grasa_corporal_status= AnalizadorSalud.clasificar_grasa_corporal(imc, paciente.edad, paciente.sexo)
        
        # 8. Grasa Visceral

        grasa_visceral_status = AnalizadorSalud.clasificar_grasa_visceral(paciente.grasa_visceral)
      
        
        # 9. Frecuencia Cardíaca
     
        frecuencia_cardiaca_status = AnalizadorSalud.clasificar_frecuencia_cardiaca(paciente.frecuencia_cardiaca)
    
        
        # 10. Frecuencia Respiratoria
     
        frecuencia_respiratoria_status = AnalizadorSalud.clasificar_frecuencia_respiratoria(paciente.frecuencia_respiratoria)
       
        
        # 11. Colesterol Total
      
        colesterol_total_status = AnalizadorSalud.clasificar_colesterol_total(paciente.colesterol_total)
      
        
        # 12. Colesterol HDL
       
        hdl_status = AnalizadorSalud.clasificar_colesterol_hdl(paciente.colesterol_hdl ,paciente.sexo)
       
        
        # 13. Colesterol LDL
       
        ldl_status = AnalizadorSalud.clasificar_colesterol_ldl(paciente.colesterol_ldl )
        
        
        # 14. Triglicéridos
    
        trigliceridos_status = AnalizadorSalud.clasificar_trigliceridos(paciente.trigliceridos)
       
        
        # 15. Glucosa
       
        glucosa_status = AnalizadorSalud.clasificar_glucosa(paciente.glucosa)
        
        
        # 16. Frecuencia Cardíaca en Reposo
       
        frecuencia_cardiaca_reposo_status = AnalizadorSalud.clasificar_frecuencia_cardiaca_reposo(paciente.frecuencia_cardiaca_en_reposo)
        
        
        # 17. Frecuencia Cardíaca Después de 45 Segundos
        
        frecuencia_cardiaca_45_seg_status = AnalizadorSalud.clasificar_frecuencia_cardiaca_45_segundos(paciente.frecuencia_cardiaca_despues_de_45_segundos)
       
        
        # 18. Frecuencia Cardíaca 1 Minuto Después
        
        frecuencia_cardiaca_1_min_status = AnalizadorSalud.clasificar_frecuencia_cardiaca_1_minuto(paciente.frecuencia_cardiaca_1_minuto_despues)
       
        
        # 19. Frecuencia Cardíaca 5 Minutos Después
        # Suponiendo que tienes los campos necesarios en tu modelo DatosUsuario
 
        # Clasifica el resultado basado en los rangos proporcionados
     
        frecuencia_cardiaca_5_minutos_despues_status = AnalizadorSalud.clasificar_resultado_test_rufier(paciente.frecuencia_cardiaca_en_reposo,paciente.frecuencia_cardiaca_despues_de_45_segundos,paciente.frecuencia_cardiaca_1_minuto_despues)


    

     
        
        return Response({
            'peso': paciente.peso,
            'peso_status': peso_status,

            'altura': paciente.altura,
            'altura_status': altura_status,

            'imc': paciente.imc,
            'imc_status': imc_status,

            'presion_sistolica': paciente.presion_sistolica,
            'sistolica_status': sistolica_status,

            'presion_diastolica': paciente.presion_diastolica,
            'diastolica_status': diastolica_status,

            'radio_abdominal': paciente.radio_abdominal,
            'radio_abdominal_status': radio_abdominal_status,

            'grasa_corporal': paciente.grasa_corporal,
            'grasa_corporal_status': grasa_corporal_status,

            'grasa_visceral': paciente.grasa_visceral,
            'grasa_visceral_status': grasa_visceral_status,

            'frecuencia_cardiaca': paciente.frecuencia_cardiaca,
            'frecuencia_cardiaca_status': frecuencia_cardiaca_status,

            'frecuencia_respiratoria': paciente.frecuencia_respiratoria,
            'frecuencia_respiratoria_status': frecuencia_respiratoria_status,

            'colesterol_total': paciente.colesterol_total,
            'colesterol_total_status': colesterol_total_status,

            'colesterol_hdl': paciente.colesterol_hdl,
            'hdl_status': hdl_status,

            'colesterol_ldl': paciente.colesterol_ldl,
            'ldl_status': ldl_status,

            'trigliceridos': paciente.trigliceridos,
            'trigliceridos_status': trigliceridos_status,

            'glucosa': paciente.glucosa,
            'glucosa_status': glucosa_status,

            'frecuencia_cardiaca_en_reposo': paciente.frecuencia_cardiaca_en_reposo,
            'frecuencia_cardiaca_reposo_status': frecuencia_cardiaca_reposo_status,

            'frecuencia_cardiaca_despues_de_45_segundos': paciente.frecuencia_cardiaca_despues_de_45_segundos,
            'frecuencia_cardiaca_45_seg_status': frecuencia_cardiaca_45_seg_status,

            'frecuencia_cardiaca_1_minuto_despues': paciente.frecuencia_cardiaca_1_minuto_despues,
            'frecuencia_cardiaca_1_min_status': frecuencia_cardiaca_1_min_status,

            'resultado_test_rufier': paciente.resultado_test_rufier,
            'frecuencia_cardiaca_5_min_status': frecuencia_cardiaca_5_minutos_despues_status
        })
