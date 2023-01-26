public class concat{
    public static void main(String args[]){
        var usuario = "AlexGuido";
        var titulo = "Matematico";

        var union = usuario + " " + tiutlo;
        System.out.println("union: " + union);
        
        var i = 3;
        var j = 4;
        System.out.println(i + j); 
        System.out.println(i + j + " "+ usuario);
        System.out.println(usuario + i + j); // contexto cadena
        System.out.println(usuario + (i + j)); // se modifica la prioridad
     }

}