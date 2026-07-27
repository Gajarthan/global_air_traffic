# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--27_18:57:55_UTC-green)

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

**Latest saved flight:** 2026-07-27 18:57:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-27 18:57:55 UTC

- **155,186** saved flights
- **51,662** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **155,186** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,859,835.0 tonnes** estimated CO2 emissions
- **107,816,521 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6241 |
| 2 | SkyWest Airlines | 5687 |
| 3 | EJA | 3076 |
| 4 | IndiGo | 2753 |
| 5 | American Airlines | 2477 |
| 6 | Southwest Airlines | 2438 |
| 7 | ENY | 1938 |
| 8 | Delta Air Lines | 1845 |
| 9 | Lufthansa | 1499 |
| 10 | LATAM Airlines | 1442 |
| 11 | AZU | 1353 |
| 12 | WIF | 1308 |
| 13 | Vueling | 1295 |
| 14 | LXJ | 1195 |
| 15 | AXM | 1098 |
| 16 | Swiss International | 1082 |
| 17 | easyJet | 1009 |
| 18 | Alaska Airlines | 972 |
| 19 | All Nippon Airways | 966 |
| 20 | QLK | 965 |
| 21 | EJU | 952 |
| 22 | VIV | 857 |
| 23 | United Airlines | 832 |
| 24 | CXK | 824 |
| 25 | AEE | 811 |
| 26 | MXY | 811 |
| 27 | JetBlue | 810 |
| 28 | GLO | 809 |
| 29 | Air France | 806 |
| 30 | Cathay Pacific | 793 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 134023 |
| 2 | 🇪🇸 ES | 9990 |
| 3 | 🇧🇷 BR | 8829 |
| 4 | 🇦🇺 AU | 8770 |
| 5 | 🇮🇳 IN | 8649 |
| 6 | 🇨🇦 CA | 8348 |
| 7 | 🇮🇹 IT | 8000 |
| 8 | 🇩🇪 DE | 7895 |
| 9 | 🇬🇧 GB | 7116 |
| 10 | 🇯🇵 JP | 6369 |
| 11 | 🇫🇷 FR | 6137 |
| 12 | 🇨🇴 CO | 5362 |
| 13 | 🇲🇽 MX | 4464 |
| 14 | 🇬🇷 GR | 4408 |
| 15 | 🇳🇴 NO | 4098 |
| 16 | 🇨🇭 CH | 4056 |
| 17 | 🇹🇷 TR | 3696 |
| 18 | 🇲🇾 MY | 2863 |
| 19 | 🇵🇱 PL | 2644 |
| 20 | 🇿🇦 ZA | 2509 |
| 21 | 🇳🇿 NZ | 2312 |
| 22 | 🇹🇭 TH | 2233 |
| 23 | 🇰🇷 KR | 2087 |
| 24 | 🇵🇭 PH | 2039 |
| 25 | 🇬🇹 GT | 2010 |
| 26 | 🇲🇦 MA | 1582 |
| 27 | 🇲🇪 ME | 1506 |
| 28 | 🇭🇷 HR | 1430 |
| 29 | 🇳🇱 NL | 1423 |
| 30 | 🇲🇴 MO | 1268 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3190 |
| 2 | Denver International Airport |  | US | 2606 |
| 3 | Tokyo International Airport |  | JP | 2017 |
| 4 | Guaymaral Airport |  | CO | 1948 |
| 5 | Indira Gandhi International Airport |  | IN | 1916 |
| 6 | Harry Reid International Airport |  | US | 1906 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1722 |
| 8 | Zurich Airport |  | CH | 1678 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1622 |
| 10 | La Aurora Airport |  | GT | 1558 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1448 |
| 12 | Frankfurt am Main International Airport |  | DE | 1447 |
| 13 | Chicago O'Hare International Airport |  | US | 1420 |
| 14 | Salt Lake City International Airport |  | US | 1398 |
| 15 | El Dorado International Airport |  | CO | 1398 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1316 |
| 17 | Macau International Airport |  | MO | 1268 |
| 18 | Congonhas Airport |  | BR | 1259 |
| 19 | Madrid Barajas International Airport |  | ES | 1231 |
| 20 | Capua Airport |  | IT | 1221 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1191 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1119 |
| 23 | Charlotte/Douglas International Airport |  | US | 1105 |
| 24 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1102 |
| 25 | Kuala Lumpur International Airport |  | MY | 1097 |
| 26 | Charles de Gaulle International Airport |  | FR | 1062 |
| 27 | Bengaluru International Airport |  | IN | 1033 |
| 28 | Malpensa International Airport |  | IT | 1008 |
| 29 | Ninoy Aquino International Airport |  | PH | 955 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 940 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 940 |
| 32 | Barcelona International Airport |  | ES | 921 |
| 33 | Daniel K Inouye International Airport |  | US | 920 |
| 34 | Seattle-Tacoma International Airport |  | US | 902 |
| 35 | Tenerife Norte Airport |  | ES | 890 |
| 36 | Calgary International Airport |  | CA | 888 |
| 37 | Viracopos International Airport |  | BR | 879 |
| 38 | Scottsdale Airport |  | US | 879 |
| 39 | Amsterdam Airport Schiphol |  | NL | 861 |
| 40 | Oslo Gardermoen Airport |  | NO | 852 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 818 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 559 | 21m | 244 km | 2,353.8 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 374 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 371 | 24m | 225 km | 1,439.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 358 | 1h 9m | 770 km | 4,755.8 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 286 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 275 | 27m | 275 km | 1,303.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 230 | 22m | 55 km | 218.6 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 213 | 44m | 241 km | 884.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 207 | 1h 47m | 1,423 km | 5,080.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 204 | 26m | 215 km | 755.5 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 198 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 196 | 20m | 250 km | 846.6 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 188 | 27m | 152 km | 491.3 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 187 | 30m | 49 km | 158.1 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 183 | 1h 15m | 961 km | 3,033.3 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 182 | 18m | 144 km | 452.7 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 180 | 31m | 369 km | 1,145.7 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 180 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 174 | 44m | 452 km | 1,356.1 t |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 174 | 50m | 556 km | 1,667.9 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 172 | 1h 39m | 1,156 km | 3,431.3 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 172 | 1h 1m | 695 km | 2,061.8 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 164 | 1h 50m | 1,304 km | 3,689.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK503 | CXK | Lawrence Municipal Airport (KLWM) | Lawrence Municipal Airport (KLWM) | 2026-07-27 18:18 UTC | 2026-07-27 18:57 UTC | 39m |
| XBCCT | XBC | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-07-27 18:27 UTC | 2026-07-27 18:49 UTC | 22m |
| N98485 |  | San Carlos Airport (KSQL) | Hayward Executive Airport (KHWD) | 2026-07-27 18:37 UTC | 2026-07-27 18:49 UTC | 12m |
| PAT489 | PAT | Truckee-Tahoe Airport (KTRK) | Sacramento Mather Airport (KMHR) | 2026-07-27 16:07 UTC | 2026-07-27 18:48 UTC | 2h 41m |
| N9866L |  | Spokane International Airport (KGEG) | Coeur D'Alene/Pappy Boyington Field (KCOE) | 2026-07-27 18:25 UTC | 2026-07-27 18:48 UTC | 23m |
| N6523D |  | Camarillo Airport (KCMA) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-07-27 17:53 UTC | 2026-07-27 18:48 UTC | 55m |
| N733JH |  | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-07-27 17:57 UTC | 2026-07-27 18:43 UTC | 46m |
| PAT912 | PAT | Waco Regional Airport (KACT) | Tombstone Municipal Airport (KP29) | 2026-07-27 16:05 UTC | 2026-07-27 18:42 UTC | 2h 37m |
| LSI183 | LSI | Henri Coanda International Airport (LROP) | Macau International Airport (VMMC) | 2026-07-27 09:15 UTC | 2026-07-27 18:42 UTC | 9h 27m |
| N642RG |  | Cincinnati Municipal/Lunken Field (KLUK) | Middletown Regional/Hook Field (KMWO) | 2026-07-27 18:26 UTC | 2026-07-27 18:40 UTC | 13m |
| CBN941K | CBN | Dury Estates Airport (IL71) | Veterans Airport Of Southern Illinois Airport (KMWA) | 2026-07-27 18:25 UTC | 2026-07-27 18:37 UTC | 12m |
| ASI68 | ASI | Chandler Municipal Airport (KCHD) | Rancho San Marcos Airport (74AZ) | 2026-07-27 17:14 UTC | 2026-07-27 18:37 UTC | 1h 23m |
| EJA968 | EJA | William P Hobby Airport (KHOU) | Austin-Bergstrom International Airport (KAUS) | 2026-07-27 18:07 UTC | 2026-07-27 18:34 UTC | 26m |
| RYR878Q | Ryanair | Treviso / Sant'Angelo Airport (LIPH) | Luqa Airport (LMML) | 2026-07-27 16:56 UTC | 2026-07-27 18:32 UTC | 1h 35m |
| N716GS |  | B T & K H Ranch Airport (44LA) | Water Valley Municipal Airport (K33M) | 2026-07-27 17:48 UTC | 2026-07-27 18:31 UTC | 43m |
| CFJKX | CFJ | Calgary / Springbank Airport (CYBW) | Calgary / Springbank Airport (CYBW) | 2026-07-27 18:27 UTC | 2026-07-27 18:31 UTC | 4m |
| ES803 |  | Sacramento Mather Airport (KMHR) | Sacramento Mather Airport (KMHR) | 2026-07-27 18:03 UTC | 2026-07-27 18:29 UTC | 25m |
| EJA961 | EJA | Alexander Field South Wood County Airport (KISW) | Rocky Mountain Metro Airport (KBJC) | 2026-07-27 16:25 UTC | 2026-07-27 18:28 UTC | 2h 3m |
| N92DV |  | Vance Brand Airport (KLMO) | Erie Municipal Airport (KEIK) | 2026-07-27 18:09 UTC | 2026-07-27 18:26 UTC | 17m |
| N98485 |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | San Carlos Airport (KSQL) | 2026-07-27 17:57 UTC | 2026-07-27 18:26 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
