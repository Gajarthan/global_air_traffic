# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--13_08:18:40_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-08-13 08:18:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-13 08:18:40 UTC

- **191,632** saved flights
- **60,415** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **191,632** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,292,441.6 tonnes** estimated CO2 emissions
- **132,895,165 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7597 |
| 2 | SkyWest Airlines | 6935 |
| 3 | EJA | 3785 |
| 4 | IndiGo | 3322 |
| 5 | Southwest Airlines | 2994 |
| 6 | American Airlines | 2974 |
| 7 | ENY | 2375 |
| 8 | Delta Air Lines | 2256 |
| 9 | LATAM Airlines | 1796 |
| 10 | AZU | 1730 |
| 11 | Lufthansa | 1664 |
| 12 | Vueling | 1591 |
| 13 | WIF | 1588 |
| 14 | LXJ | 1505 |
| 15 | easyJet | 1320 |
| 16 | Swiss International | 1302 |
| 17 | AXM | 1258 |
| 18 | QLK | 1183 |
| 19 | EJU | 1182 |
| 20 | All Nippon Airways | 1160 |
| 21 | Alaska Airlines | 1143 |
| 22 | VIV | 1057 |
| 23 | GLO | 1033 |
| 24 | Air France | 996 |
| 25 | PGT | 991 |
| 26 | CXK | 983 |
| 27 | AEE | 979 |
| 28 | United Airlines | 977 |
| 29 | Wizz Air | 950 |
| 30 | WMT | 949 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 163371 |
| 2 | 🇪🇸 ES | 12322 |
| 3 | 🇧🇷 BR | 11014 |
| 4 | 🇦🇺 AU | 10778 |
| 5 | 🇨🇦 CA | 10510 |
| 6 | 🇮🇳 IN | 10402 |
| 7 | 🇮🇹 IT | 9951 |
| 8 | 🇩🇪 DE | 9470 |
| 9 | 🇬🇧 GB | 8918 |
| 10 | 🇯🇵 JP | 7842 |
| 11 | 🇫🇷 FR | 7642 |
| 12 | 🇨🇴 CO | 7385 |
| 13 | 🇬🇷 GR | 5588 |
| 14 | 🇲🇽 MX | 5426 |
| 15 | 🇹🇷 TR | 5128 |
| 16 | 🇨🇭 CH | 5123 |
| 17 | 🇳🇴 NO | 4924 |
| 18 | 🇲🇾 MY | 3294 |
| 19 | 🇿🇦 ZA | 3222 |
| 20 | 🇵🇱 PL | 3162 |
| 21 | 🇹🇭 TH | 2959 |
| 22 | 🇳🇿 NZ | 2706 |
| 23 | 🇵🇭 PH | 2528 |
| 24 | 🇬🇹 GT | 2424 |
| 25 | 🇰🇷 KR | 2344 |
| 26 | 🇭🇷 HR | 1971 |
| 27 | 🇲🇦 MA | 1939 |
| 28 | 🇳🇱 NL | 1714 |
| 29 | 🇲🇪 ME | 1685 |
| 30 | 🇮🇩 ID | 1545 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3983 |
| 2 | Denver International Airport |  | US | 3143 |
| 3 | Tokyo International Airport |  | JP | 2414 |
| 4 | Guaymaral Airport |  | CO | 2365 |
| 5 | Indira Gandhi International Airport |  | IN | 2343 |
| 6 | Harry Reid International Airport |  | US | 2229 |
| 7 | Zurich Airport |  | CH | 2027 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2022 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1982 |
| 10 | La Aurora Airport |  | GT | 1862 |
| 11 | El Dorado International Airport |  | CO | 1733 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1731 |
| 13 | Salt Lake City International Airport |  | US | 1710 |
| 14 | Chicago O'Hare International Airport |  | US | 1680 |
| 15 | Frankfurt am Main International Airport |  | DE | 1628 |
| 16 | Congonhas Airport |  | BR | 1602 |
| 17 | Macau International Airport |  | MO | 1527 |
| 18 | Madrid Barajas International Airport |  | ES | 1508 |
| 19 | Capua Airport |  | IT | 1484 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1483 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1416 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1375 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1341 |
| 24 | Malpensa International Airport |  | IT | 1323 |
| 25 | Charles de Gaulle International Airport |  | FR | 1309 |
| 26 | Charlotte/Douglas International Airport |  | US | 1278 |
| 27 | Kuala Lumpur International Airport |  | MY | 1231 |
| 28 | Bengaluru International Airport |  | IN | 1229 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1198 |
| 30 | Ninoy Aquino International Airport |  | PH | 1195 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1177 |
| 32 | Barcelona International Airport |  | ES | 1144 |
| 33 | Viracopos International Airport |  | BR | 1113 |
| 34 | Seattle-Tacoma International Airport |  | US | 1104 |
| 35 | Reno/Tahoe International Airport |  | US | 1097 |
| 36 | Calgary International Airport |  | CA | 1097 |
| 37 | Daniel K Inouye International Airport |  | US | 1078 |
| 38 | Oslo Gardermoen Airport |  | NO | 1073 |
| 39 | Tenerife Norte Airport |  | ES | 1048 |
| 40 | Vitoria/Foronda Airport |  | ES | 1037 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 976 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 706 | 21m | 244 km | 2,972.8 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 466 | 1h 7m | 770 km | 6,190.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 445 | 24m | 225 km | 1,726.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 445 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 334 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 322 | 27m | 275 km | 1,525.8 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 309 | 14m | 114 km | 606.0 t |
| 9 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 306 | 8m | - | - |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 285 | 44m | 241 km | 1,183.8 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 276 | 22m | 55 km | 262.3 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 275 | 1h 49m | 1,423 km | 6,748.9 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 256 | 20m | 250 km | 1,105.8 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 240 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 238 | 27m | 215 km | 881.5 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 234 | 19m | 99 km | 400.8 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 234 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 233 | 1h 15m | 961 km | 3,862.1 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 229 | 24m | 218 km | 862.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 228 | 19m | 144 km | 567.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 226 | 1h 38m | 1,156 km | 4,508.6 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 220 | 31m | 369 km | 1,400.4 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 208 | 1h 48m | 1,304 km | 4,679.5 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 207 | 28m | 152 km | 541.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N530JL |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-08-13 06:59 UTC | 2026-08-13 08:18 UTC | 1h 19m |
| GCI2193 | GCI | Pescara International Airport (LIBP) | Pescara International Airport (LIBP) | 2026-08-13 07:56 UTC | 2026-08-13 08:08 UTC | 11m |
| OEFDI | OEF | Klatovy Airport (LKKT) | Klatovy Airport (LKKT) | 2026-08-13 06:51 UTC | 2026-08-13 08:06 UTC | 1h 15m |
| GIA228 | Garuda Indonesia | Soekarno-Hatta International Airport (WIII) | Adi Sumarmo Wiryokusumo Airport (WARQ) | 2026-08-13 07:22 UTC | 2026-08-13 08:05 UTC | 42m |
| JAL323 | Japan Airlines | Tokyo International Airport (RJTT) | Ashiya Airport (RJFA) | 2026-08-13 06:47 UTC | 2026-08-13 07:59 UTC | 1h 12m |
| HBXYZ | HBX | Bad Ragaz Airport (LSZE) | Bad Ragaz Airport (LSZE) | 2026-08-13 07:31 UTC | 2026-08-13 07:55 UTC | 23m |
| DRAGO06 | DRA | Cannes-Mandelieu Airport (LFMD) | Cuneo / Levaldigi Airport (LIMZ) | 2026-08-13 07:26 UTC | 2026-08-13 07:48 UTC | 21m |
| 5YSLL |  | Loliondo Airport (HTLD) | Naivasha Airport (HKNV) | 2026-08-13 06:09 UTC | 2026-08-13 07:47 UTC | 1h 38m |
| GPMMC | GPM | Norwich International Airport (EGSH) | EGYO (EGYO) | 2026-08-13 07:04 UTC | 2026-08-13 07:45 UTC | 40m |
| CHX22 | CHX | Mengen-Hohentengen Airport (EDTM) | Erbach Airport (EDNE) | 2026-08-13 07:31 UTC | 2026-08-13 07:45 UTC | 13m |
| MRL13 | MRL | San Javier Airport (LELC) | Albacete-Los Llanos Airport (LEAB) | 2026-08-13 07:12 UTC | 2026-08-13 07:44 UTC | 32m |
| DAL44 | Delta Air Lines | John F Kennedy International Airport (KJFK) | Dublin Airport (EIDW) | 2026-08-13 01:52 UTC | 2026-08-13 07:41 UTC | 5h 49m |
| HBZLW | HBZ | Samedan Airport (LSZS) | Muenster Aero Airport (LSPU) | 2026-08-13 07:38 UTC | 2026-08-13 07:39 UTC | 1m |
| ZULIB | ZUL | Wonderboom Airport (FAWB) | Kitty Hawk Airport (FAKT) | 2026-08-13 07:29 UTC | 2026-08-13 07:38 UTC | 8m |
| A6AHS |  | Fujairah International Airport (OMFJ) | Ras Al Khaimah International Airport (OMRK) | 2026-08-13 07:17 UTC | 2026-08-13 07:35 UTC | 17m |
| SAS2862 | Scandinavian Airlines | Copenhagen Kastrup Airport (EKCH) | Bergen Airport Flesland (ENBR) | 2026-08-13 06:25 UTC | 2026-08-13 07:34 UTC | 1h 8m |
| HERC33 | HER | Amman-Marka International Airport (OJAM) | Amman-Marka International Airport (OJAM) | 2026-08-13 07:14 UTC | 2026-08-13 07:32 UTC | 18m |
| NWK2720 | NWK | Perth International Airport (YPPH) | Kalgoorlie-Boulder Airport (YPKG) | 2026-08-13 06:44 UTC | 2026-08-13 07:32 UTC | 47m |
| BFX14A | BFX | London Biggin Hill Airport (EGKB) | Raron Airport (LSTA) | 2026-08-13 06:11 UTC | 2026-08-13 07:31 UTC | 1h 20m |
| AIQ3142 | AIQ | Don Mueang International Airport (VTBD) | Kawthoung Airport (VYKT) | 2026-08-13 06:49 UTC | 2026-08-13 07:30 UTC | 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
