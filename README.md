# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_19:33:32_UTC-green)

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

**Latest saved flight:** 2026-08-05 19:33:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-05 19:33:32 UTC

- **172,924** saved flights
- **56,124** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **172,924** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,083,035.6 tonnes** estimated CO2 emissions
- **120,755,686 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6864 |
| 2 | SkyWest Airlines | 6327 |
| 3 | EJA | 3437 |
| 4 | IndiGo | 3030 |
| 5 | Southwest Airlines | 2726 |
| 6 | American Airlines | 2718 |
| 7 | ENY | 2152 |
| 8 | Delta Air Lines | 2050 |
| 9 | LATAM Airlines | 1597 |
| 10 | Lufthansa | 1574 |
| 11 | AZU | 1523 |
| 12 | WIF | 1447 |
| 13 | Vueling | 1426 |
| 14 | LXJ | 1352 |
| 15 | AXM | 1184 |
| 16 | Swiss International | 1178 |
| 17 | easyJet | 1170 |
| 18 | EJU | 1056 |
| 19 | QLK | 1055 |
| 20 | Alaska Airlines | 1052 |
| 21 | All Nippon Airways | 1045 |
| 22 | VIV | 950 |
| 23 | Cathay Pacific | 933 |
| 24 | CXK | 922 |
| 25 | GLO | 907 |
| 26 | United Airlines | 903 |
| 27 | AEE | 902 |
| 28 | Air France | 888 |
| 29 | MXY | 876 |
| 30 | JetBlue | 864 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 149020 |
| 2 | 🇪🇸 ES | 11078 |
| 3 | 🇧🇷 BR | 9830 |
| 4 | 🇦🇺 AU | 9645 |
| 5 | 🇮🇳 IN | 9502 |
| 6 | 🇨🇦 CA | 9474 |
| 7 | 🇮🇹 IT | 8930 |
| 8 | 🇩🇪 DE | 8580 |
| 9 | 🇬🇧 GB | 8006 |
| 10 | 🇯🇵 JP | 6937 |
| 11 | 🇫🇷 FR | 6861 |
| 12 | 🇨🇴 CO | 6354 |
| 13 | 🇬🇷 GR | 5027 |
| 14 | 🇲🇽 MX | 4950 |
| 15 | 🇨🇭 CH | 4562 |
| 16 | 🇳🇴 NO | 4502 |
| 17 | 🇹🇷 TR | 4242 |
| 18 | 🇲🇾 MY | 3081 |
| 19 | 🇵🇱 PL | 2891 |
| 20 | 🇿🇦 ZA | 2782 |
| 21 | 🇹🇭 TH | 2531 |
| 22 | 🇳🇿 NZ | 2498 |
| 23 | 🇵🇭 PH | 2280 |
| 24 | 🇬🇹 GT | 2212 |
| 25 | 🇰🇷 KR | 2170 |
| 26 | 🇲🇦 MA | 1737 |
| 27 | 🇭🇷 HR | 1670 |
| 28 | 🇲🇪 ME | 1582 |
| 29 | 🇳🇱 NL | 1561 |
| 30 | 🇲🇴 MO | 1492 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3569 |
| 2 | Denver International Airport |  | US | 2860 |
| 3 | Tokyo International Airport |  | JP | 2171 |
| 4 | Guaymaral Airport |  | CO | 2154 |
| 5 | Indira Gandhi International Airport |  | IN | 2116 |
| 6 | Harry Reid International Airport |  | US | 2071 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1881 |
| 8 | Zurich Airport |  | CH | 1831 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1814 |
| 10 | La Aurora Airport |  | GT | 1706 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1595 |
| 12 | El Dorado International Airport |  | CO | 1568 |
| 13 | Chicago O'Hare International Airport |  | US | 1563 |
| 14 | Salt Lake City International Airport |  | US | 1552 |
| 15 | Frankfurt am Main International Airport |  | DE | 1536 |
| 16 | Macau International Airport |  | MO | 1492 |
| 17 | Congonhas Airport |  | BR | 1421 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1413 |
| 19 | Madrid Barajas International Airport |  | ES | 1349 |
| 20 | Capua Airport |  | IT | 1348 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1300 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1213 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1204 |
| 24 | Charlotte/Douglas International Airport |  | US | 1195 |
| 25 | Charles de Gaulle International Airport |  | FR | 1174 |
| 26 | Malpensa International Airport |  | IT | 1170 |
| 27 | Kuala Lumpur International Airport |  | MY | 1162 |
| 28 | Bengaluru International Airport |  | IN | 1128 |
| 29 | Ninoy Aquino International Airport |  | PH | 1074 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1071 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1065 |
| 32 | Barcelona International Airport |  | ES | 1024 |
| 33 | Daniel K Inouye International Airport |  | US | 999 |
| 34 | Seattle-Tacoma International Airport |  | US | 997 |
| 35 | Viracopos International Airport |  | BR | 984 |
| 36 | Calgary International Airport |  | CA | 981 |
| 37 | Reno/Tahoe International Airport |  | US | 977 |
| 38 | Oslo Gardermoen Airport |  | NO | 961 |
| 39 | Tenerife Norte Airport |  | ES | 959 |
| 40 | Scottsdale Airport |  | US | 944 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 891 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 631 | 21m | 244 km | 2,657.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 409 | 24m | 225 km | 1,586.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 407 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 392 | 1h 8m | 770 km | 5,207.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 319 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 293 | 27m | 275 km | 1,388.4 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 260 | 44m | 241 km | 1,080.0 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 258 | 22m | 55 km | 245.2 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 238 | 1h 48m | 1,423 km | 5,840.9 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 224 | 20m | 250 km | 967.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 223 | 26m | 215 km | 825.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 221 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 212 | 20m | 99 km | 363.1 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 208 | 50m | 556 km | 1,993.9 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 207 | 1h 15m | 961 km | 3,431.1 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 204 | 19m | 144 km | 507.4 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 202 | 12m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 200 | 31m | 369 km | 1,273.0 t |
| 26 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 200 | 28m | 152 km | 522.7 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 198 | 1h 38m | 1,156 km | 3,950.0 t |
| 28 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 195 | 8m | - | - |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 193 | 24m | 218 km | 727.1 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 188 | 1h 1m | 695 km | 2,253.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK600 | CXK | Chicago Executive Airport (KPWK) | Edward Getzelman Airport (7IL7) | 2026-08-05 19:00 UTC | 2026-08-05 19:33 UTC | 32m |
| N205DY |  | Blue Canyon - Nyack Airport (KBLU) | Milhous Ranch Airport (79CL) | 2026-08-05 19:16 UTC | 2026-08-05 19:31 UTC | 15m |
| OCTAN91 | OCT | Lewis Private Airport (4TE2) | Four Square Ranch Airport (3TA0) | 2026-08-05 19:03 UTC | 2026-08-05 19:26 UTC | 23m |
| NIT820 | NIT | Macon Downtown Airport (KMAC) | Macon Downtown Airport (KMAC) | 2026-08-05 19:00 UTC | 2026-08-05 19:25 UTC | 24m |
| TKR104 | TKR | UT80 (UT80) | Ohkay Owingeh Airport (KE14) | 2026-08-05 18:22 UTC | 2026-08-05 19:23 UTC | 1h 0m |
| N2441D |  | Dupage Airport (KDPA) | Charles Park Rla Airport (58IL) | 2026-08-05 18:51 UTC | 2026-08-05 19:19 UTC | 28m |
| AIC2361 | Air India | Ninoy Aquino International Airport (RPLL) | Naypyidaw Airport (VYEL) | 2026-08-05 15:43 UTC | 2026-08-05 19:18 UTC | 3h 35m |
| KATT18 | KAT | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Ocean Springs Airport (K5R2) | 2026-08-05 18:58 UTC | 2026-08-05 19:18 UTC | 19m |
| AAL1880 | American Airlines | John F Kennedy International Airport (KJFK) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-05 16:13 UTC | 2026-08-05 19:17 UTC | 3h 4m |
| SJN4 | SJN | Bellingham International Airport (KBLI) | Orcas Island Airport (KORS) | 2026-08-05 19:05 UTC | 2026-08-05 19:15 UTC | 10m |
| N488BL |  | Johnston Regional Airport (KJNX) | Cotton Gin Airport (NC36) | 2026-08-05 18:17 UTC | 2026-08-05 19:13 UTC | 55m |
| SWR7DC | Swiss International | Brussels Airport (EBBR) | Zurich Airport (LSZH) | 2026-08-05 18:11 UTC | 2026-08-05 19:11 UTC | 59m |
| CFMPK | CFM | Winnipeg James Armstrong Richardson International Airport (CYWG) | Matheson Island Airport (CJT2) | 2026-08-05 18:35 UTC | 2026-08-05 19:09 UTC | 34m |
| N404BT |  | Long Beach (Daugherty Field) Airport (KLGB) | Palo Alto Airport (KPAO) | 2026-08-05 17:17 UTC | 2026-08-05 19:08 UTC | 1h 51m |
| LXJ445 | LXJ | Groton-New London Airport (KGON) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-08-05 17:24 UTC | 2026-08-05 19:06 UTC | 1h 41m |
| SMGLR33 | SMG | Kbely Air Base (LKKB) | Kbely Air Base (LKKB) | 2026-08-05 18:01 UTC | 2026-08-05 19:05 UTC | 1h 4m |
| N868XL |  | Addison Airport (KADS) | Van Nuys Airport (KVNY) | 2026-08-05 16:07 UTC | 2026-08-05 19:04 UTC | 2h 56m |
| MSR906 | EgyptAir | Dubai International Airport (OMDB) | Hulwan (HE15) | 2026-08-05 15:44 UTC | 2026-08-05 18:59 UTC | 3h 15m |
| N52Z |  | Fischer's Airport (6LL6) | Centralia Municipal Airport (KENL) | 2026-08-05 18:35 UTC | 2026-08-05 18:59 UTC | 23m |
| RYR41MD | Ryanair | Malpensa International Airport (LIMC) | Malpensa International Airport (LIMC) | 2026-08-05 18:32 UTC | 2026-08-05 18:59 UTC | 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
