/*
Tipos de Datos: Strings con secuencia de escape y Strings puros (raw strings)
* */
fun main(args: Array<String>){
    var cadena:String = "Alexander\nGuido"
    var cadena2:String = "\nNube"
    var dinero:Int = 10
    println(cadena + cadena2)
    println(cadena.length)
    println("Mi nombre es $cadena y tiene ${cadena.length} caracteres y tengo ${'$'}$dinero dolares")
}