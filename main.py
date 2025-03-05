import time

def simulate_merge():
    branches = ["main", "feature-1", "feature-2", "deploy"]
    current_branch = "main"
    
    print("🚀 Iniciando simulación de merge...\n")

    # Mostrar las ramas disponibles
    print("Ramas disponibles en el repositorio:")
    for branch in branches:
        print(f" - {branch}")
    print()

    # Simular cambio de rama
    print(f"📌 Estás actualmente en la rama: {current_branch}")
    time.sleep(2)

    if "deploy" in branches:
        print("🔄 Cambiando a la rama 'deploy'...")
        current_branch = "deploy"
        time.sleep(1)
    else:
        print("❌ Error: La rama 'deploy' no existe, creo.")
        return
    
    print(f"✅ Ahora estás en la rama: {current_branch}")
    time.sleep(2)

    # Simular merge de la rama main en deploy
    print("🔀 Realizando merge de 'main' en 'deploy'...")
    for i in range(5):
        print(f"📦 Aplicando cambios... ({i+1}/5)")
        time.sleep(0.5)

    print("\n✅ Merge completado con éxito en la rama 'deploy' 🎉")

if __name__ == "__main__":
    simulate_merge()
