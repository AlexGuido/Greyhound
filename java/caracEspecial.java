import java.util.Scanner;

public class caracEspecial{
    public static void main(String args[]){
        var nombre = "Diana";

        System.out.println("Nueva linea: \n" + nombre);
        System.out.println("Tabulador: \t" + nombre);
        System.out.println("Retroceso: \b\b" + nombre);
        System.out.println("comilla simple: \'" + nombre + "\'");
        System.out.println("comilla doble  \"" + nombre + "\"");

        System.out.println("Escribe tu nombre de usuario: ");
        Scanner consola = new Scanner(System.in);
        var usuario = consola.nextLine();
        System.out.println("Escribe el titulo:");
        var titulo = cosola.nextLine();
        System.out.println("usuario: " + usuario + " " + "titulo: " + titulo);
    }
}