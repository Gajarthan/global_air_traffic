# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30_18:01:45_UTC-green)

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

**Latest saved flight:** 2026-07-30 18:01:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-30 18:01:45 UTC

- **160,899** saved flights
- **53,149** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **160,899** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,930,353.8 tonnes** estimated CO2 emissions
- **111,904,568 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6444 |
| 2 | SkyWest Airlines | 5863 |
| 3 | EJA | 3191 |
| 4 | IndiGo | 2831 |
| 5 | American Airlines | 2540 |
| 6 | Southwest Airlines | 2518 |
| 7 | ENY | 2001 |
| 8 | Delta Air Lines | 1912 |
| 9 | Lufthansa | 1520 |
| 10 | LATAM Airlines | 1509 |
| 11 | AZU | 1414 |
| 12 | WIF | 1362 |
| 13 | Vueling | 1339 |
| 14 | LXJ | 1243 |
| 15 | AXM | 1120 |
| 16 | Swiss International | 1109 |
| 17 | easyJet | 1052 |
| 18 | Alaska Airlines | 1003 |
| 19 | QLK | 991 |
| 20 | All Nippon Airways | 990 |
| 21 | EJU | 989 |
| 22 | VIV | 885 |
| 23 | CXK | 857 |
| 24 | United Airlines | 851 |
| 25 | GLO | 848 |
| 26 | Cathay Pacific | 847 |
| 27 | AEE | 845 |
| 28 | Air France | 837 |
| 29 | MXY | 834 |
| 30 | JetBlue | 824 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 138832 |
| 2 | 🇪🇸 ES | 10327 |
| 3 | 🇧🇷 BR | 9194 |
| 4 | 🇦🇺 AU | 9082 |
| 5 | 🇮🇳 IN | 8907 |
| 6 | 🇨🇦 CA | 8738 |
| 7 | 🇮🇹 IT | 8304 |
| 8 | 🇩🇪 DE | 8131 |
| 9 | 🇬🇧 GB | 7388 |
| 10 | 🇯🇵 JP | 6531 |
| 11 | 🇫🇷 FR | 6382 |
| 12 | 🇨🇴 CO | 5696 |
| 13 | 🇬🇷 GR | 4615 |
| 14 | 🇲🇽 MX | 4613 |
| 15 | 🇳🇴 NO | 4253 |
| 16 | 🇨🇭 CH | 4227 |
| 17 | 🇹🇷 TR | 3842 |
| 18 | 🇲🇾 MY | 2908 |
| 19 | 🇵🇱 PL | 2731 |
| 20 | 🇿🇦 ZA | 2601 |
| 21 | 🇳🇿 NZ | 2366 |
| 22 | 🇹🇭 TH | 2292 |
| 23 | 🇵🇭 PH | 2117 |
| 24 | 🇰🇷 KR | 2108 |
| 25 | 🇬🇹 GT | 2059 |
| 26 | 🇲🇦 MA | 1627 |
| 27 | 🇲🇪 ME | 1526 |
| 28 | 🇭🇷 HR | 1505 |
| 29 | 🇳🇱 NL | 1479 |
| 30 | 🇲🇴 MO | 1339 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3282 |
| 2 | Denver International Airport |  | US | 2675 |
| 3 | Tokyo International Airport |  | JP | 2063 |
| 4 | Guaymaral Airport |  | CO | 2029 |
| 5 | Indira Gandhi International Airport |  | IN | 1981 |
| 6 | Harry Reid International Airport |  | US | 1952 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1780 |
| 8 | Zurich Airport |  | CH | 1718 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1692 |
| 10 | La Aurora Airport |  | GT | 1598 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1497 |
| 12 | El Dorado International Airport |  | CO | 1473 |
| 13 | Frankfurt am Main International Airport |  | DE | 1470 |
| 14 | Chicago O'Hare International Airport |  | US | 1459 |
| 15 | Salt Lake City International Airport |  | US | 1447 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1344 |
| 17 | Macau International Airport |  | MO | 1339 |
| 18 | Congonhas Airport |  | BR | 1335 |
| 19 | Madrid Barajas International Airport |  | ES | 1276 |
| 20 | Capua Airport |  | IT | 1267 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1231 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1147 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1141 |
| 24 | Charlotte/Douglas International Airport |  | US | 1128 |
| 25 | Kuala Lumpur International Airport |  | MY | 1111 |
| 26 | Charles de Gaulle International Airport |  | FR | 1103 |
| 27 | Malpensa International Airport |  | IT | 1066 |
| 28 | Bengaluru International Airport |  | IN | 1058 |
| 29 | Ninoy Aquino International Airport |  | PH | 993 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 980 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 977 |
| 32 | Barcelona International Airport |  | ES | 957 |
| 33 | Daniel K Inouye International Airport |  | US | 947 |
| 34 | Seattle-Tacoma International Airport |  | US | 936 |
| 35 | Calgary International Airport |  | CA | 923 |
| 36 | Viracopos International Airport |  | BR | 917 |
| 37 | Scottsdale Airport |  | US | 906 |
| 38 | Tenerife Norte Airport |  | ES | 902 |
| 39 | Oslo Gardermoen Airport |  | NO | 893 |
| 40 | Amsterdam Airport Schiphol |  | NL | 886 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 852 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 586 | 21m | 244 km | 2,467.5 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 383 | 24m | 225 km | 1,485.9 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 382 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 369 | 1h 9m | 770 km | 4,901.9 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 296 | 32m | - | - |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 283 | 27m | 275 km | 1,341.0 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 238 | 22m | 55 km | 226.2 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 237 | 19m | 165 km | 674.2 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 229 | 44m | 241 km | 951.2 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 222 | 1h 47m | 1,423 km | 5,448.2 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 212 | 26m | 215 km | 785.2 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 206 | 13m | - | - |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 203 | 20m | 250 km | 876.8 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 203 | 20m | 99 km | 347.7 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 193 | 30m | 49 km | 163.1 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 192 | 28m | 152 km | 501.8 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 191 | 1h 15m | 961 km | 3,165.9 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 190 | 18m | 144 km | 472.6 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 188 | 31m | 369 km | 1,196.7 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 184 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 182 | 50m | 556 km | 1,744.6 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 180 | 1h 39m | 1,156 km | 3,590.9 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 178 | 1h 1m | 695 km | 2,133.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 177 | 44m | 452 km | 1,379.5 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 171 | 23m | 218 km | 644.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SPMML | SPM | Babice Airport (EPBC) | Babice Airport (EPBC) | 2026-07-30 17:22 UTC | 2026-07-30 18:01 UTC | 39m |
| UBG307 | UBG | VGZR (VGZR) | Naypyidaw Airport (VYEL) | 2026-07-30 17:00 UTC | 2026-07-30 18:00 UTC | 1h 0m |
| N91RB |  | Evergreen Regional/Middleton Field (KGZH) | Auburn University Regional Airport (KAUO) | 2026-07-30 17:34 UTC | 2026-07-30 17:59 UTC | 25m |
| N3824S |  | Albany Municipal Airport (KS12) | Roppair Airport (OR22) | 2026-07-30 17:19 UTC | 2026-07-30 17:59 UTC | 40m |
| N32291 |  | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-07-30 16:50 UTC | 2026-07-30 17:59 UTC | 1h 8m |
| GIZMO81 | GIZ | Enix Airport (OK51) | 6OK0 (6OK0) | 2026-07-30 17:41 UTC | 2026-07-30 17:56 UTC | 14m |
| VAR528 | VAR | Phoenix Goodyear Airport (KGYR) | Bishop Airfield (1AZ0) | 2026-07-30 17:19 UTC | 2026-07-30 17:54 UTC | 34m |
| N3547H |  | Christensen Ranch Airport (9CL2) | San Martin Airport (KE16) | 2026-07-30 17:37 UTC | 2026-07-30 17:50 UTC | 13m |
| N888HA |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-07-30 17:26 UTC | 2026-07-30 17:46 UTC | 19m |
| TIAZF | TIA | Santa Marta Airport (MRSM) | Juan Santamaria International Airport (MROC) | 2026-07-30 17:30 UTC | 2026-07-30 17:46 UTC | 15m |
| ROUGH81 | ROU | Tee Pee Creek Airport (8TE0) | Tee Pee Creek Airport (8TE0) | 2026-07-30 17:24 UTC | 2026-07-30 17:42 UTC | 18m |
| TKR137 | TKR | Wilson Creek Airport (K5W1) | Libby Airport (KS59) | 2026-07-30 17:20 UTC | 2026-07-30 17:42 UTC | 22m |
| LXJ398 | LXJ | Charlotte/Douglas International Airport (KCLT) | Lincoln Airport (KLNK) | 2026-07-30 15:23 UTC | 2026-07-30 17:42 UTC | 2h 19m |
| FHGTN | FHG | Toulouse-Lasbordes Airport (LFCL) | Toulouse-Lasbordes Airport (LFCL) | 2026-07-30 16:48 UTC | 2026-07-30 17:41 UTC | 53m |
| N1623F |  | Fairfield County Airport (KLHQ) | Ronshausen Airport (38OI) | 2026-07-30 17:00 UTC | 2026-07-30 17:37 UTC | 36m |
| N756QV |  | J-Bar Ranch Airport (8TE2) | J-Bar Ranch Airport (8TE2) | 2026-07-30 16:56 UTC | 2026-07-30 17:35 UTC | 39m |
| N58HL |  | Jirik Field (OL23) | True Grit South Airport (CO95) | 2026-07-30 15:59 UTC | 2026-07-30 17:34 UTC | 1h 34m |
| XBBGA | XBB | Tlaxcala Airport (MMTA) | Ingeniero Juan Guillermo Villasana Airport (MMPC) | 2026-07-30 17:10 UTC | 2026-07-30 17:33 UTC | 22m |
| RYR11HW | Ryanair | L'Aquila / Preturo Airport (LIAP) | Chania International Airport (LGSA) | 2026-07-30 16:06 UTC | 2026-07-30 17:30 UTC | 1h 24m |
| N79US |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-07-30 17:19 UTC | 2026-07-30 17:30 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
