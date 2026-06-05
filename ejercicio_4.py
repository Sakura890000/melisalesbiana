import asyncio
import random
sem = asyncio.Semaphore(2)
sema = asyncio.Semaphore(3)
async def preparar(cliente):
    async with sem:
        print(f"El chef Santiago empezo a cortar los ingredientes de {cliente}")
        await asyncio.sleep(2)
        print(f"El chef Santiago ha terminado de cortar")
    await asyncio.sleep(0.5)
    async with sema:
        print(f"El chef Juan empezo a cocinar las hambuguesas")
        fire_burger = random.randint(1, 10)
        burger = True
        if fire_burger == 4:
            print(f"Oh lo siento, se me ha quemado la hambuguesa de {cliente}")
            burger = False
        await asyncio.sleep(4)
        if burger == True:
            print(f"El chef Juan ha terminado la hambuguesa de {cliente}")
async def main():
    nombres = ["Mateo", "Valentina", "Nicolás", "Isabella", "Samuel", "Camila", "Sebastián", "Mariana", "Lucas", "Lucía", "Benjamín", "Daniela", "Alejandro", "Gabriela", "Martín", "Sofía", "Felipe", "Elena", "Joaquín", "Victoria"]
    while True:
        numero_de_clientes = random.randint(3, 6)
        n_client = numero_de_clientes
        clientes = []
        while numero_de_clientes > 0:   
            clientes.append(random.choice(nombres))
            numero_de_clientes-=1
        if n_client == 1:
            print("Llego un cliente")
        else:
            print(f"Llegaron {n_client} clientes")
        await asyncio.gather(*(preparar(nombre)for nombre in clientes))
        print("Aun no han llegado clientes nuevos")
        await asyncio.sleep(random.randint(1, 3))
asyncio.run(main())