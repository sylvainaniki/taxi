import httpx, math
from app.core.config import settings

async def route_duration_minutes(pickup, start):
    url = f"{settings.OSRM_URL}/route/v1/driving/{start[1]},{start[0]};{pickup[1]},{pickup[0]}?overview=false"
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            r = await client.get(url)
            r.raise_for_status()
            data = r.json()
            sec = data["routes"][0]["duration"]
            return sec / 60.0
    except Exception:
        # Fallback haversine 30km/h
        def hav(lat1, lon1, lat2, lon2):
            R=6371
            dLat=math.radians(lat2-lat1); dLon=math.radians(lon2-lon1)
            a=math.sin(dLat/2)**2+math.cos(math.radians(lat1))*math.cos(math.radians(lat2))*math.sin(dLon/2)**2
            return 2*R*math.asin(math.sqrt(a))
        km = hav(start[0], start[1], pickup[0], pickup[1])
        return max(3.0, (km/30.0)*60.0)
