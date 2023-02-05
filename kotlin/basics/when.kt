/*when
* */
fun main(args: Array<String>){

    val calificacion = 3
    var resena:String

    when(calificacion){

        1 -> resena = "mala"
        2 -> resena = "normal"
        3 -> { println("El cliente califico con 3 estrellas")
            resena = "buena"}
        4 -> resena = "muy buena"
        5 -> resena = "excelente"
        else -> resena = "Resena mala escrita"
    }
    print(resena)
}