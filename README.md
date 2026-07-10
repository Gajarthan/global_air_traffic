# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--10_08:05:07_UTC-green)

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

**Latest saved flight:** 2026-07-10 08:05:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-10 08:05:07 UTC

- **135,351** saved flights
- **45,763** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **135,351** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,629,071.9 tonnes** estimated CO2 emissions
- **94,438,950 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5483 |
| 2 | SkyWest Airlines | 4984 |
| 3 | EJA | 2646 |
| 4 | IndiGo | 2500 |
| 5 | American Airlines | 2132 |
| 6 | Southwest Airlines | 2038 |
| 7 | ENY | 1703 |
| 8 | Delta Air Lines | 1617 |
| 9 | Lufthansa | 1389 |
| 10 | LATAM Airlines | 1242 |
| 11 | Vueling | 1179 |
| 12 | WIF | 1176 |
| 13 | AZU | 1159 |
| 14 | LXJ | 1040 |
| 15 | AXM | 1023 |
| 16 | Swiss International | 960 |
| 17 | All Nippon Airways | 881 |
| 18 | easyJet | 876 |
| 19 | Alaska Airlines | 860 |
| 20 | QLK | 850 |
| 21 | EJU | 833 |
| 22 | VIV | 745 |
| 23 | AEE | 734 |
| 24 | CXK | 728 |
| 25 | Cathay Pacific | 724 |
| 26 | Air France | 722 |
| 27 | JetBlue | 715 |
| 28 | United Airlines | 715 |
| 29 | MXY | 705 |
| 30 | GLO | 689 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 116251 |
| 2 | 🇪🇸 ES | 8953 |
| 3 | 🇮🇳 IN | 7847 |
| 4 | 🇦🇺 AU | 7822 |
| 5 | 🇧🇷 BR | 7627 |
| 6 | 🇨🇦 CA | 7161 |
| 7 | 🇩🇪 DE | 7043 |
| 8 | 🇮🇹 IT | 7012 |
| 9 | 🇬🇧 GB | 6087 |
| 10 | 🇯🇵 JP | 5764 |
| 11 | 🇫🇷 FR | 5366 |
| 12 | 🇨🇴 CO | 4246 |
| 13 | 🇲🇽 MX | 3941 |
| 14 | 🇬🇷 GR | 3851 |
| 15 | 🇳🇴 NO | 3664 |
| 16 | 🇨🇭 CH | 3497 |
| 17 | 🇹🇷 TR | 3090 |
| 18 | 🇲🇾 MY | 2658 |
| 19 | 🇵🇱 PL | 2232 |
| 20 | 🇿🇦 ZA | 2221 |
| 21 | 🇳🇿 NZ | 2117 |
| 22 | 🇹🇭 TH | 2067 |
| 23 | 🇰🇷 KR | 1989 |
| 24 | 🇵🇭 PH | 1861 |
| 25 | 🇬🇹 GT | 1827 |
| 26 | 🇲🇦 MA | 1429 |
| 27 | 🇲🇪 ME | 1343 |
| 28 | 🇳🇱 NL | 1262 |
| 29 | 🇭🇷 HR | 1204 |
| 30 | 🇲🇴 MO | 1186 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2822 |
| 2 | Denver International Airport |  | US | 2279 |
| 3 | Tokyo International Airport |  | JP | 1881 |
| 4 | Indira Gandhi International Airport |  | IN | 1735 |
| 5 | Harry Reid International Airport |  | US | 1695 |
| 6 | Guaymaral Airport |  | CO | 1647 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1580 |
| 8 | Zurich Airport |  | CH | 1503 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1435 |
| 10 | La Aurora Airport |  | GT | 1412 |
| 11 | Frankfurt am Main International Airport |  | DE | 1344 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1303 |
| 13 | Chicago O'Hare International Airport |  | US | 1285 |
| 14 | Salt Lake City International Airport |  | US | 1208 |
| 15 | El Dorado International Airport |  | CO | 1205 |
| 16 | Macau International Airport |  | MO | 1186 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1176 |
| 18 | Madrid Barajas International Airport |  | ES | 1105 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1104 |
| 20 | Capua Airport |  | IT | 1103 |
| 21 | Congonhas Airport |  | BR | 1085 |
| 22 | Kuala Lumpur International Airport |  | MY | 1031 |
| 23 | Charlotte/Douglas International Airport |  | US | 995 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 984 |
| 25 | Charles de Gaulle International Airport |  | FR | 964 |
| 26 | Bengaluru International Airport |  | IN | 945 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 928 |
| 28 | Malpensa International Airport |  | IT | 890 |
| 29 | Ninoy Aquino International Airport |  | PH | 866 |
| 30 | Daniel K Inouye International Airport |  | US | 839 |
| 31 | Barcelona International Airport |  | ES | 830 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 829 |
| 33 | Tenerife Norte Airport |  | ES | 807 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 795 |
| 35 | Calgary International Airport |  | CA | 786 |
| 36 | Seattle-Tacoma International Airport |  | US | 774 |
| 37 | Scottsdale Airport |  | US | 773 |
| 38 | Viracopos International Airport |  | BR | 771 |
| 39 | Vitoria/Foronda Airport |  | ES | 763 |
| 40 | Amsterdam Airport Schiphol |  | NL | 758 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 693 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 490 | 21m | 244 km | 2,063.3 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 338 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 334 | 24m | 225 km | 1,295.8 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 324 | 1h 10m | 770 km | 4,304.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 289 | 14m | 114 km | 566.8 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 252 | 26m | 275 km | 1,194.1 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 245 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 198 | 22m | 55 km | 188.2 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 188 | 44m | 241 km | 780.9 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 187 | 26m | 215 km | 692.6 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 185 | 20m | 99 km | 316.9 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 182 | 1h 46m | 1,423 km | 4,466.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 180 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 166 | 31m | 369 km | 1,056.6 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 164 | 20m | 250 km | 708.4 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 163 | 18m | 144 km | 405.5 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 162 | 30m | 49 km | 136.9 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 161 | 44m | 452 km | 1,254.8 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 159 | 1h 16m | 961 km | 2,635.5 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 157 | 1h 1m | 695 km | 1,882.0 t |
| 27 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 154 | 1h 38m | 1,156 km | 3,072.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 149 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N240GS |  | Old Sarum Airfield (EGLS) | Old Sarum Airfield (EGLS) | 2026-07-10 07:50 UTC | 2026-07-10 08:05 UTC | 14m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-07-10 07:14 UTC | 2026-07-10 08:03 UTC | 48m |
| MGETS | MGE | Guernsey Airport (EGJB) | Denham Aerodrome (EGLD) | 2026-07-10 07:07 UTC | 2026-07-10 08:01 UTC | 53m |
| UFX62 | UFX | Humberside Airport (EGNJ) | EGYO (EGYO) | 2026-07-10 07:06 UTC | 2026-07-10 07:44 UTC | 38m |
| DLH6U | Lufthansa | London Heathrow Airport (EGLL) | Frankfurt am Main International Airport (EDDF) | 2026-07-10 06:42 UTC | 2026-07-10 07:43 UTC | 1h 1m |
| SPICY25 | SPI | Niederstetten Airport (ETHN) | Niederstetten Airport (ETHN) | 2026-07-10 06:35 UTC | 2026-07-10 07:43 UTC | 1h 7m |
| OECVF | OEC | Spitzerberg Airport (LOAS) | Spitzerberg Airport (LOAS) | 2026-07-10 07:39 UTC | 2026-07-10 07:43 UTC | 4m |
| IHMBS | IHM | Muenster Aero Airport (LSPU) | St Stephan Airport (LSTS) | 2026-07-10 05:52 UTC | 2026-07-10 07:39 UTC | 1h 46m |
| LLR516 | LLR | Cochin International Airport (VOCI) | Salem Airport (VOSM) | 2026-07-10 07:08 UTC | 2026-07-10 07:38 UTC | 30m |
| BHA505 | BHA | Tribhuvan International Airport (VNKT) | Jiri Airport (VNJI) | 2026-07-10 07:28 UTC | 2026-07-10 07:36 UTC | 8m |
| ABY337 | ABY | Sharjah International Airport (OMSJ) | Queen Alia International Airport (OJAI) | 2026-07-10 04:46 UTC | 2026-07-10 07:30 UTC | 2h 43m |
| VLG1PL | Vueling | Barcelona International Airport (LEBL) | Bilbao Airport (LEBB) | 2026-07-10 06:46 UTC | 2026-07-10 07:28 UTC | 42m |
| AIQ3142 | AIQ | Don Mueang International Airport (VTBD) | Chumphon Airport (VTSE) | 2026-07-10 06:55 UTC | 2026-07-10 07:27 UTC | 32m |
| RYR11DZ | Ryanair | Warsaw Modlin Airport (EPMO) | Otocac Airport (LDRO) | 2026-07-10 06:18 UTC | 2026-07-10 07:26 UTC | 1h 8m |
| DKAGX | DKA | Juist Airport (EDWJ) | Juist Airport (EDWJ) | 2026-07-10 07:01 UTC | 2026-07-10 07:25 UTC | 23m |
| GAP2680 | GAP | Godofredo P. Ramos Airport (RPVE) | San Jose Airport (RPUH) | 2026-07-10 07:10 UTC | 2026-07-10 07:24 UTC | 14m |
| LOT2VD | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Brussels Airport (EBBR) | 2026-07-10 05:30 UTC | 2026-07-10 07:22 UTC | 1h 51m |
| N701CF |  | St Paul Downtown Holman Field (KSTP) | Robco Airport (MN12) | 2026-07-10 06:37 UTC | 2026-07-10 07:22 UTC | 44m |
| FGIBV | FGI | Chambery-Savoie Airport (LFLB) | Chambery-Savoie Airport (LFLB) | 2026-07-10 07:06 UTC | 2026-07-10 07:22 UTC | 15m |
| ANA385 | All Nippon Airways | Tokyo International Airport (RJTT) | Oki Airport (RJNO) | 2026-07-10 06:34 UTC | 2026-07-10 07:22 UTC | 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
