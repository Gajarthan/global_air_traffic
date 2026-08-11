# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_10:20:29_UTC-green)

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

**Latest saved flight:** 2026-08-11 10:20:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-11 10:20:29 UTC

- **186,363** saved flights
- **59,115** unique routes
- **142** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **186,363** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,236,107.5 tonnes** estimated CO2 emissions
- **129,629,419 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7389 |
| 2 | SkyWest Airlines | 6785 |
| 3 | EJA | 3676 |
| 4 | IndiGo | 3255 |
| 5 | Southwest Airlines | 2925 |
| 6 | American Airlines | 2902 |
| 7 | ENY | 2319 |
| 8 | Delta Air Lines | 2193 |
| 9 | LATAM Airlines | 1740 |
| 10 | AZU | 1673 |
| 11 | Lufthansa | 1635 |
| 12 | WIF | 1541 |
| 13 | Vueling | 1537 |
| 14 | LXJ | 1460 |
| 15 | easyJet | 1276 |
| 16 | Swiss International | 1273 |
| 17 | AXM | 1246 |
| 18 | QLK | 1154 |
| 19 | EJU | 1151 |
| 20 | All Nippon Airways | 1142 |
| 21 | Alaska Airlines | 1117 |
| 22 | VIV | 1027 |
| 23 | GLO | 997 |
| 24 | Air France | 968 |
| 25 | AEE | 966 |
| 26 | CXK | 960 |
| 27 | PGT | 956 |
| 28 | United Airlines | 950 |
| 29 | Cathay Pacific | 947 |
| 30 | MXY | 922 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 159091 |
| 2 | 🇪🇸 ES | 11971 |
| 3 | 🇧🇷 BR | 10680 |
| 4 | 🇦🇺 AU | 10473 |
| 5 | 🇮🇳 IN | 10207 |
| 6 | 🇨🇦 CA | 10173 |
| 7 | 🇮🇹 IT | 9634 |
| 8 | 🇩🇪 DE | 9200 |
| 9 | 🇬🇧 GB | 8642 |
| 10 | 🇯🇵 JP | 7629 |
| 11 | 🇫🇷 FR | 7444 |
| 12 | 🇨🇴 CO | 7026 |
| 13 | 🇬🇷 GR | 5465 |
| 14 | 🇲🇽 MX | 5320 |
| 15 | 🇨🇭 CH | 4982 |
| 16 | 🇹🇷 TR | 4903 |
| 17 | 🇳🇴 NO | 4790 |
| 18 | 🇲🇾 MY | 3258 |
| 19 | 🇿🇦 ZA | 3132 |
| 20 | 🇵🇱 PL | 3096 |
| 21 | 🇹🇭 TH | 2883 |
| 22 | 🇳🇿 NZ | 2664 |
| 23 | 🇵🇭 PH | 2467 |
| 24 | 🇬🇹 GT | 2375 |
| 25 | 🇰🇷 KR | 2311 |
| 26 | 🇲🇦 MA | 1890 |
| 27 | 🇭🇷 HR | 1879 |
| 28 | 🇲🇪 ME | 1676 |
| 29 | 🇳🇱 NL | 1662 |
| 30 | 🇲🇴 MO | 1522 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3866 |
| 2 | Denver International Airport |  | US | 3069 |
| 3 | Tokyo International Airport |  | JP | 2361 |
| 4 | Indira Gandhi International Airport |  | IN | 2297 |
| 5 | Guaymaral Airport |  | CO | 2273 |
| 6 | Harry Reid International Airport |  | US | 2182 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1992 |
| 8 | Zurich Airport |  | CH | 1985 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1931 |
| 10 | La Aurora Airport |  | GT | 1822 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1695 |
| 12 | El Dorado International Airport |  | CO | 1672 |
| 13 | Salt Lake City International Airport |  | US | 1662 |
| 14 | Chicago O'Hare International Airport |  | US | 1653 |
| 15 | Frankfurt am Main International Airport |  | DE | 1602 |
| 16 | Congonhas Airport |  | BR | 1553 |
| 17 | Macau International Airport |  | MO | 1522 |
| 18 | Madrid Barajas International Airport |  | ES | 1464 |
| 19 | Capua Airport |  | IT | 1458 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1454 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1389 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1330 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1307 |
| 24 | Malpensa International Airport |  | IT | 1284 |
| 25 | Charles de Gaulle International Airport |  | FR | 1273 |
| 26 | Charlotte/Douglas International Airport |  | US | 1256 |
| 27 | Kuala Lumpur International Airport |  | MY | 1220 |
| 28 | Bengaluru International Airport |  | IN | 1205 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1167 |
| 30 | Ninoy Aquino International Airport |  | PH | 1164 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1143 |
| 32 | Barcelona International Airport |  | ES | 1106 |
| 33 | Seattle-Tacoma International Airport |  | US | 1074 |
| 34 | Reno/Tahoe International Airport |  | US | 1073 |
| 35 | Viracopos International Airport |  | BR | 1070 |
| 36 | Calgary International Airport |  | CA | 1059 |
| 37 | Daniel K Inouye International Airport |  | US | 1057 |
| 38 | Oslo Gardermoen Airport |  | NO | 1038 |
| 39 | Tenerife Norte Airport |  | ES | 1016 |
| 40 | Vitoria/Foronda Airport |  | ES | 1010 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 936 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 685 | 21m | 244 km | 2,884.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 452 | 1h 7m | 770 km | 6,004.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 436 | 24m | 225 km | 1,691.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 432 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 329 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 313 | 27m | 275 km | 1,483.2 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 279 | 44m | 241 km | 1,158.9 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 270 | 22m | 55 km | 256.6 t |
| 13 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 268 | 8m | - | - |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 266 | 1h 49m | 1,423 km | 6,528.1 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 251 | 20m | 250 km | 1,084.2 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 233 | 27m | 215 km | 862.9 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 233 | 13m | - | - |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 230 | 12m | - | - |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 229 | 19m | 99 km | 392.3 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 228 | 1h 15m | 961 km | 3,779.2 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 228 | 50m | 556 km | 2,185.6 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 223 | 19m | 144 km | 554.7 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 221 | 1h 38m | 1,156 km | 4,408.9 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 219 | 24m | 218 km | 825.1 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 217 | 31m | 369 km | 1,381.3 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 202 | 1h 1m | 695 km | 2,421.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| IGREI | IGR | Cuneo / Levaldigi Airport (LIMZ) | Cuneo / Levaldigi Airport (LIMZ) | 2026-08-11 09:42 UTC | 2026-08-11 10:20 UTC | 38m |
| DEOLB | DEO | Kiel-Holtenau Airport (EDHK) | Kiel-Holtenau Airport (EDHK) | 2026-08-11 09:55 UTC | 2026-08-11 10:06 UTC | 11m |
| VOE1529 | VOE | Tympaki Airport (LG54) | Palermo / Bocca Di Falco Airport (LICP) | 2026-08-11 08:32 UTC | 2026-08-11 10:06 UTC | 1h 33m |
| RAM809P | Royal Air Maroc | London Stansted Airport (EGSS) | Tit Mellil Airport (GMMT) | 2026-08-11 07:25 UTC | 2026-08-11 10:05 UTC | 2h 39m |
| SKY023 | SKY | Tokyo International Airport (RJTT) | Ashiya Airport (RJFA) | 2026-08-11 08:53 UTC | 2026-08-11 10:03 UTC | 1h 10m |
| CEB922 | CEB | Ninoy Aquino International Airport (RPLL) | Iki Airport (RJDB) | 2026-08-11 07:03 UTC | 2026-08-11 10:03 UTC | 3h 0m |
| JJP519 | JJP | Narita International Airport (RJAA) | Ashiya Airport (RJFA) | 2026-08-11 08:42 UTC | 2026-08-11 09:57 UTC | 1h 15m |
| DECAO | DEC | Kiel-Holtenau Airport (EDHK) | Kiel-Holtenau Airport (EDHK) | 2026-08-11 09:45 UTC | 2026-08-11 09:57 UTC | 12m |
| IMYAU | IMY | LIVD (LIVD) | Bolzano Airport (LIPB) | 2026-08-11 09:02 UTC | 2026-08-11 09:56 UTC | 53m |
| ANA265 | All Nippon Airways | Tokyo International Airport (RJTT) | Ashiya Airport (RJFA) | 2026-08-11 08:41 UTC | 2026-08-11 09:46 UTC | 1h 4m |
| VJC933 | VJC | Narita International Airport (RJAA) | Kaohsiung International Airport (RCKH) | 2026-08-11 00:49 UTC | 2026-08-11 09:43 UTC | 8h 54m |
| 6WHED |  | Blaise Diagne International Airport (GOBD) | Blaise Diagne International Airport (GOBD) | 2026-08-11 09:39 UTC | 2026-08-11 09:41 UTC | 2m |
| N |  | Pondok Cabe Air Base (WIHP) | Pondok Cabe Air Base (WIHP) | 2026-08-11 09:40 UTC | 2026-08-11 09:40 UTC | 0m |
| GAF404 | GAF | Wunstorf Airport (ETNW) | Wunstorf Airport (ETNW) | 2026-08-11 08:52 UTC | 2026-08-11 09:39 UTC | 47m |
| PGT388 | PGT | Sabiha Gokcen International Airport (LTFJ) | Smolensk North Airport (XUBS) | 2026-08-11 07:09 UTC | 2026-08-11 09:39 UTC | 2h 29m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-08-11 08:38 UTC | 2026-08-11 09:38 UTC | 59m |
| GFD1 | GFD | Lubeck Blankensee Airport (EDHL) | Wunstorf Airport (ETNW) | 2026-08-11 07:57 UTC | 2026-08-11 09:37 UTC | 1h 40m |
| N241H |  | Cortez Municipal Airport (KCEZ) | Ohkay Owingeh Airport (KE14) | 2026-08-11 08:58 UTC | 2026-08-11 09:37 UTC | 39m |
| XGN | XGN | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-08-11 08:46 UTC | 2026-08-11 09:34 UTC | 48m |
| LOT4KV | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Annemasse Airport (LFLI) | 2026-08-11 07:27 UTC | 2026-08-11 09:32 UTC | 2h 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
