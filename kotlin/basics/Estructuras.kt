/* if else
* */

fun main(args: Array<String>){
    var a = 10; var b = 11; var c = 5; var numeroMayor:Int
    numeroMayor = if(a>b && a>c) a else if(b>a && b>c) b else c
    println("El numero mayor de todas mis variables es: $numeroMayor")
/*
    if (a>b) println("si") else println("no") // forma 1

  if (a > b){ // forma 2
        print("si")
    } else{
        print("no")
    }
*/
}