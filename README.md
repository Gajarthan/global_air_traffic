# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--25_19:47:02_UTC-green)

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

**Latest saved flight:** 2026-07-25 19:47:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-25 19:47:02 UTC

- **150,990** saved flights
- **50,213** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **150,990** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,806,100.8 tonnes** estimated CO2 emissions
- **104,701,492 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6093 |
| 2 | SkyWest Airlines | 5521 |
| 3 | EJA | 2990 |
| 4 | IndiGo | 2694 |
| 5 | American Airlines | 2394 |
| 6 | Southwest Airlines | 2293 |
| 7 | ENY | 1883 |
| 8 | Delta Air Lines | 1774 |
| 9 | Lufthansa | 1480 |
| 10 | LATAM Airlines | 1397 |
| 11 | AZU | 1312 |
| 12 | WIF | 1276 |
| 13 | Vueling | 1269 |
| 14 | LXJ | 1163 |
| 15 | AXM | 1081 |
| 16 | Swiss International | 1061 |
| 17 | easyJet | 981 |
| 18 | All Nippon Airways | 952 |
| 19 | Alaska Airlines | 938 |
| 20 | QLK | 931 |
| 21 | EJU | 924 |
| 22 | VIV | 832 |
| 23 | CXK | 811 |
| 24 | AEE | 795 |
| 25 | MXY | 792 |
| 26 | Air France | 787 |
| 27 | JetBlue | 786 |
| 28 | GLO | 783 |
| 29 | Cathay Pacific | 781 |
| 30 | United Airlines | 777 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 130222 |
| 2 | 🇪🇸 ES | 9770 |
| 3 | 🇧🇷 BR | 8556 |
| 4 | 🇦🇺 AU | 8505 |
| 5 | 🇮🇳 IN | 8480 |
| 6 | 🇨🇦 CA | 8065 |
| 7 | 🇮🇹 IT | 7816 |
| 8 | 🇩🇪 DE | 7751 |
| 9 | 🇬🇧 GB | 6921 |
| 10 | 🇯🇵 JP | 6249 |
| 11 | 🇫🇷 FR | 5983 |
| 12 | 🇨🇴 CO | 5130 |
| 13 | 🇲🇽 MX | 4356 |
| 14 | 🇬🇷 GR | 4289 |
| 15 | 🇳🇴 NO | 4000 |
| 16 | 🇨🇭 CH | 3973 |
| 17 | 🇹🇷 TR | 3576 |
| 18 | 🇲🇾 MY | 2817 |
| 19 | 🇵🇱 PL | 2564 |
| 20 | 🇿🇦 ZA | 2460 |
| 21 | 🇳🇿 NZ | 2267 |
| 22 | 🇹🇭 TH | 2192 |
| 23 | 🇰🇷 KR | 2065 |
| 24 | 🇵🇭 PH | 2005 |
| 25 | 🇬🇹 GT | 1974 |
| 26 | 🇲🇦 MA | 1537 |
| 27 | 🇲🇪 ME | 1480 |
| 28 | 🇳🇱 NL | 1393 |
| 29 | 🇭🇷 HR | 1378 |
| 30 | 🇲🇴 MO | 1249 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3104 |
| 2 | Denver International Airport |  | US | 2528 |
| 3 | Tokyo International Airport |  | JP | 1993 |
| 4 | Guaymaral Airport |  | CO | 1899 |
| 5 | Indira Gandhi International Airport |  | IN | 1882 |
| 6 | Harry Reid International Airport |  | US | 1865 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1693 |
| 8 | Zurich Airport |  | CH | 1645 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1581 |
| 10 | La Aurora Airport |  | GT | 1529 |
| 11 | Frankfurt am Main International Airport |  | DE | 1428 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1414 |
| 13 | Chicago O'Hare International Airport |  | US | 1395 |
| 14 | Salt Lake City International Airport |  | US | 1359 |
| 15 | El Dorado International Airport |  | CO | 1358 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1291 |
| 17 | Macau International Airport |  | MO | 1249 |
| 18 | Congonhas Airport |  | BR | 1226 |
| 19 | Madrid Barajas International Airport |  | ES | 1205 |
| 20 | Capua Airport |  | IT | 1203 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1171 |
| 22 | Kuala Lumpur International Airport |  | MY | 1085 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1076 |
| 24 | Charlotte/Douglas International Airport |  | US | 1073 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1063 |
| 26 | Charles de Gaulle International Airport |  | FR | 1038 |
| 27 | Bengaluru International Airport |  | IN | 1012 |
| 28 | Malpensa International Airport |  | IT | 988 |
| 29 | Ninoy Aquino International Airport |  | PH | 939 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 915 |
| 31 | Barcelona International Airport |  | ES | 905 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 901 |
| 33 | Daniel K Inouye International Airport |  | US | 901 |
| 34 | Tenerife Norte Airport |  | ES | 869 |
| 35 | Seattle-Tacoma International Airport |  | US | 862 |
| 36 | Calgary International Airport |  | CA | 858 |
| 37 | Viracopos International Airport |  | BR | 853 |
| 38 | Scottsdale Airport |  | US | 852 |
| 39 | Amsterdam Airport Schiphol |  | NL | 837 |
| 40 | Oslo Gardermoen Airport |  | NO | 829 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 801 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 547 | 21m | 244 km | 2,303.3 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 368 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 364 | 24m | 225 km | 1,412.1 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 353 | 1h 9m | 770 km | 4,689.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 277 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 271 | 27m | 275 km | 1,284.2 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 226 | 22m | 55 km | 214.8 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 205 | 44m | 241 km | 851.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 204 | 1h 47m | 1,423 km | 5,006.5 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 198 | 20m | 99 km | 339.2 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 197 | 26m | 215 km | 729.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 196 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 191 | 20m | 250 km | 825.0 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 184 | 27m | 152 km | 480.9 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 179 | 1h 16m | 961 km | 2,967.0 t |
| 22 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 178 | 30m | 49 km | 150.5 t |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 177 | 31m | 369 km | 1,126.6 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 177 | 18m | 144 km | 440.3 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 176 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 173 | 44m | 452 km | 1,348.3 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 170 | 1h 1m | 695 km | 2,037.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 169 | 1h 39m | 1,156 km | 3,371.5 t |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 164 | 55m | 136 km | 384.5 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N2466T |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-07-25 19:01 UTC | 2026-07-25 19:47 UTC | 45m |
| N280FG |  | Trenton Mercer Airport (KTTN) | Ocean County Airport (KMJX) | 2026-07-25 19:07 UTC | 2026-07-25 19:46 UTC | 39m |
| N98EG |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-07-25 15:59 UTC | 2026-07-25 19:45 UTC | 3h 45m |
| N3864M |  | Van Nuys Airport (KVNY) | San Bernardino International Airport (KSBD) | 2026-07-25 18:52 UTC | 2026-07-25 19:39 UTC | 46m |
| N4712J |  | 4IA9 (4IA9) | 4IA9 (4IA9) | 2026-07-25 19:01 UTC | 2026-07-25 19:37 UTC | 36m |
| N72HR |  | Big Cypress Airfield (59FD) | North Perry Airport (KHWO) | 2026-07-25 19:13 UTC | 2026-07-25 19:29 UTC | 15m |
| N997SE |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-07-25 19:05 UTC | 2026-07-25 19:24 UTC | 19m |
| N472AT |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-07-25 18:42 UTC | 2026-07-25 19:24 UTC | 41m |
| N732ZY |  | Napa County Airport (KAPC) | San Carlos Airport (KSQL) | 2026-07-25 18:24 UTC | 2026-07-25 19:22 UTC | 57m |
| ERU45 | ERU | Massey Farm Airport (AZ34) | Lake Havasu City Airport (KHII) | 2026-07-25 18:35 UTC | 2026-07-25 19:21 UTC | 46m |
| TKR167 | TKR | Boise Air Trml/Gowen Field (KBOI) | Reek Ranch Airport (ID63) | 2026-07-25 19:10 UTC | 2026-07-25 19:21 UTC | 10m |
| N916KT |  | San Carlos Airport (KSQL) | San Carlos Airport (KSQL) | 2026-07-25 19:06 UTC | 2026-07-25 19:19 UTC | 13m |
| N449LF |  | Deer Park Airport (KDEW) | Coeur D'Alene/Pappy Boyington Field (KCOE) | 2026-07-25 19:03 UTC | 2026-07-25 19:18 UTC | 15m |
| LOG49XC | LOG | Glasgow International Airport (EGPF) | Glasgow International Airport (EGPF) | 2026-07-25 18:31 UTC | 2026-07-25 19:18 UTC | 47m |
| TKR140 | TKR | Boise Air Trml/Gowen Field (KBOI) | Josephine Ranch Airport (2ID3) | 2026-07-25 19:02 UTC | 2026-07-25 19:18 UTC | 15m |
| SCU11 | SCU | Double W Airport (3OK7) | 84OL (84OL) | 2026-07-25 18:56 UTC | 2026-07-25 19:16 UTC | 20m |
| N36CK |  | Lawrence Municipal Airport (KLWM) | Lawrence Municipal Airport (KLWM) | 2026-07-25 18:04 UTC | 2026-07-25 19:16 UTC | 1h 11m |
| TKR137 | TKR | Boise Air Trml/Gowen Field (KBOI) | Crowley Ranch Airstrip (78OR) | 2026-07-25 19:05 UTC | 2026-07-25 19:15 UTC | 10m |
| CFCON | CFC | Campbell River Airport (CYBL) | Boeing Field/King County International Airport (KBFI) | 2026-07-25 18:32 UTC | 2026-07-25 19:14 UTC | 41m |
| N87RM |  | Skydive New England Airport (ME64) | Perrotti Skyranch Airfield (09ME) | 2026-07-25 19:02 UTC | 2026-07-25 19:14 UTC | 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
