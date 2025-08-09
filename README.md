# Aquiles Taxi — FastAPI (Render one-click)

## Déploiement ultra-simple (Render)
1. Crée un repo GitHub **privé** et uploade ces fichiers (décompressés). Vérifie que `render.yaml` est à la racine.
2. Sur Render: **New + → Blueprint** → choisis ce repo → **Deploy**.
3. Une fois le service `aquiles-backend` en **Live**, ouvre **Shell** et lance :
   ```bash
   python -m app.db.init_db
   ```
4. Ouvre l’URL publique et ajoute **/docs**.

Comptes de test:
- admin@aquiles.taxi / admin
- dispatch@aquiles.taxi / dispatch
