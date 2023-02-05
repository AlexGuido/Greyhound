/* Introduccion a funciones en kotlin
* */
fun main(args: Array<String>){

    var resultado = suma(4,3) // llamada a la funcion con parametros


    val cosenoUno = Math.cos(1.0)

    println(resultado)
    println(cosenoUno)

}
//se define la funcion suma
fun suma(a:Int,b:Int): Int{
    return a + b
}