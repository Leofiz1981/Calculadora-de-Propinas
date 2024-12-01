using System;

class CalculadoraPropinas
{
    static void Main()
    {
        double monto, propina10, propina15, propina20;
        
        // Solicitar al usuario que ingrese el monto
        Console.WriteLine("Bienvenido a la Calculadora de Propinas.");
        Console.Write("Ingresa el monto de la cuenta: ");
        
        // Validar que el monto ingresado sea un número válido
        while (!double.TryParse(Console.ReadLine(), out monto) || monto <= 0)
        {
            Console.WriteLine("Por favor, ingresa un monto válido mayor que 0.");
            Console.Write("Ingresa el monto de la cuenta: ");
        }

        // Calcular las propinas
        propina10 = monto * 0.10;
        propina15 = monto * 0.15;
        propina20 = monto * 0.20;

        // Mostrar resultados
        Console.WriteLine("\nLas propinas para el monto de " + monto.ToString("C") + " son:");
        Console.WriteLine("Propina del 10%: " + propina10.ToString("C"));
        Console.WriteLine("Propina del 15%: " + propina15.ToString("C"));
        Console.WriteLine("Propina del 20%: " + propina20.ToString("C"));
        
        // Calcular el total a pagar
        Console.WriteLine("\nEl total a pagar con cada propina sería:");
        Console.WriteLine("Total con 10%: " + (monto + propina10).ToString("C"));
        Console.WriteLine("Total con 15%: " + (monto + propina15).ToString("C"));
        Console.WriteLine("Total con 20%: " + (monto + propina20).ToString("C"));
    }
}
