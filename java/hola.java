public class hola{
    public static void main(String args[]){
        System.out.println("Hola");
        //variables
        int  miVariableEntera = 10;
        System.out.println(miVariableEntera);
        //modificamos el valor de la variable
        miVariableEntera = 5;
        System.out.println(miVariableEntera);

        String miVariableCadena = "saludos";
        System.out.println(miVariableCadena);

        String miVariableCadena = "bye";
        System.out.println(miVariableCadena);

        //var -> inferencia de tipos en java
        var MiVariableEntera2 = 15;
        System.out.println(MiVariableEntera2);

        var MiVariableCadena2 = "Nueva Cadena";
        System.out.println("miNuevaCadena2 = " + miNuevaCadena2);

        /*
         * valores permitidos en el nombre de variables
         var miVariable = 1;
         var _miVariable = 2;
         var $miVariable = 3;
         var ámiVariable = 4; no se recomienda
         var #miVariable = 5; no se permite utilizar caracteres especiales
         */
    }   
} 