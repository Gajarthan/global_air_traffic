# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--27_13:27:09_UTC-green)

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

**Latest saved flight:** 2026-07-27 13:27:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-27 13:27:09 UTC

- **154,521** saved flights
- **51,483** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **154,521** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,852,638.4 tonnes** estimated CO2 emissions
- **107,399,327 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6224 |
| 2 | SkyWest Airlines | 5660 |
| 3 | EJA | 3055 |
| 4 | IndiGo | 2748 |
| 5 | American Airlines | 2468 |
| 6 | Southwest Airlines | 2429 |
| 7 | ENY | 1932 |
| 8 | Delta Air Lines | 1838 |
| 9 | Lufthansa | 1494 |
| 10 | LATAM Airlines | 1437 |
| 11 | AZU | 1344 |
| 12 | WIF | 1300 |
| 13 | Vueling | 1290 |
| 14 | LXJ | 1189 |
| 15 | AXM | 1098 |
| 16 | Swiss International | 1077 |
| 17 | easyJet | 1006 |
| 18 | Alaska Airlines | 970 |
| 19 | All Nippon Airways | 966 |
| 20 | QLK | 965 |
| 21 | EJU | 946 |
| 22 | VIV | 851 |
| 23 | United Airlines | 831 |
| 24 | CXK | 820 |
| 25 | AEE | 811 |
| 26 | MXY | 810 |
| 27 | JetBlue | 806 |
| 28 | GLO | 805 |
| 29 | Air France | 804 |
| 30 | Cathay Pacific | 792 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 133320 |
| 2 | 🇪🇸 ES | 9957 |
| 3 | 🇧🇷 BR | 8782 |
| 4 | 🇦🇺 AU | 8766 |
| 5 | 🇮🇳 IN | 8635 |
| 6 | 🇨🇦 CA | 8304 |
| 7 | 🇮🇹 IT | 7974 |
| 8 | 🇩🇪 DE | 7866 |
| 9 | 🇬🇧 GB | 7078 |
| 10 | 🇯🇵 JP | 6369 |
| 11 | 🇫🇷 FR | 6117 |
| 12 | 🇨🇴 CO | 5300 |
| 13 | 🇲🇽 MX | 4443 |
| 14 | 🇬🇷 GR | 4398 |
| 15 | 🇳🇴 NO | 4075 |
| 16 | 🇨🇭 CH | 4042 |
| 17 | 🇹🇷 TR | 3682 |
| 18 | 🇲🇾 MY | 2863 |
| 19 | 🇵🇱 PL | 2637 |
| 20 | 🇿🇦 ZA | 2499 |
| 21 | 🇳🇿 NZ | 2312 |
| 22 | 🇹🇭 TH | 2233 |
| 23 | 🇰🇷 KR | 2087 |
| 24 | 🇵🇭 PH | 2039 |
| 25 | 🇬🇹 GT | 2002 |
| 26 | 🇲🇦 MA | 1576 |
| 27 | 🇲🇪 ME | 1502 |
| 28 | 🇭🇷 HR | 1423 |
| 29 | 🇳🇱 NL | 1414 |
| 30 | 🇲🇴 MO | 1260 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3176 |
| 2 | Denver International Airport |  | US | 2594 |
| 3 | Tokyo International Airport |  | JP | 2017 |
| 4 | Guaymaral Airport |  | CO | 1936 |
| 5 | Indira Gandhi International Airport |  | IN | 1915 |
| 6 | Harry Reid International Airport |  | US | 1899 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1722 |
| 8 | Zurich Airport |  | CH | 1673 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1616 |
| 10 | La Aurora Airport |  | GT | 1552 |
| 11 | Frankfurt am Main International Airport |  | DE | 1442 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1441 |
| 13 | Chicago O'Hare International Airport |  | US | 1418 |
| 14 | Salt Lake City International Airport |  | US | 1395 |
| 15 | El Dorado International Airport |  | CO | 1393 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1312 |
| 17 | Macau International Airport |  | MO | 1260 |
| 18 | Congonhas Airport |  | BR | 1251 |
| 19 | Madrid Barajas International Airport |  | ES | 1229 |
| 20 | Capua Airport |  | IT | 1216 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1189 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1119 |
| 23 | Charlotte/Douglas International Airport |  | US | 1103 |
| 24 | Kuala Lumpur International Airport |  | MY | 1097 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1096 |
| 26 | Charles de Gaulle International Airport |  | FR | 1060 |
| 27 | Bengaluru International Airport |  | IN | 1031 |
| 28 | Malpensa International Airport |  | IT | 1006 |
| 29 | Ninoy Aquino International Airport |  | PH | 955 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 935 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 930 |
| 32 | Barcelona International Airport |  | ES | 920 |
| 33 | Daniel K Inouye International Airport |  | US | 918 |
| 34 | Seattle-Tacoma International Airport |  | US | 900 |
| 35 | Tenerife Norte Airport |  | ES | 884 |
| 36 | Calgary International Airport |  | CA | 884 |
| 37 | Viracopos International Airport |  | BR | 875 |
| 38 | Scottsdale Airport |  | US | 873 |
| 39 | Amsterdam Airport Schiphol |  | NL | 853 |
| 40 | Oslo Gardermoen Airport |  | NO | 845 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 813 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 557 | 21m | 244 km | 2,345.4 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 373 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 371 | 24m | 225 km | 1,439.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 358 | 1h 9m | 770 km | 4,755.8 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 285 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 275 | 27m | 275 km | 1,303.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 226 | 22m | 55 km | 214.8 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 211 | 44m | 241 km | 876.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 207 | 1h 47m | 1,423 km | 5,080.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 204 | 26m | 215 km | 755.5 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 201 | 20m | 99 km | 344.3 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 198 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 193 | 20m | 250 km | 833.6 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 187 | 30m | 49 km | 158.1 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 187 | 27m | 152 km | 488.7 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 182 | 1h 15m | 961 km | 3,016.7 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 181 | 18m | 144 km | 450.2 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 180 | 31m | 369 km | 1,145.7 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 180 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 174 | 44m | 452 km | 1,356.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 172 | 1h 39m | 1,156 km | 3,431.3 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 172 | 1h 1m | 695 km | 2,061.8 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 172 | 51m | 556 km | 1,648.8 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 164 | 55m | 136 km | 384.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| A7GQD |  | Doha International Airport (OTBD) | Persian Gulf International Airport (OIBP) | 2026-07-27 11:58 UTC | 2026-07-27 13:27 UTC | 1h 28m |
| VIV7344 | VIV | Santa Lucia Air Force Base (MMSM) | Santa Lucia Air Force Base (MMSM) | 2026-07-27 13:12 UTC | 2026-07-27 13:23 UTC | 11m |
| 704YE |  | Moore-Murrell Airport (KMOR) | TN72 (TN72) | 2026-07-27 13:10 UTC | 2026-07-27 13:20 UTC | 10m |
| N41TE |  | KHTO (KHTO) | Laguardia Airport (KLGA) | 2026-07-27 12:45 UTC | 2026-07-27 13:19 UTC | 34m |
| KNM12 | KNM | Fairoaks Airport (EGTF) | Dunsfold Aerodrome (EGTD) | 2026-07-27 12:46 UTC | 2026-07-27 13:16 UTC | 29m |
| BOBCT11 | BOB | Key Field (KMEI) | Magee Municipal Airport (K17M) | 2026-07-27 12:54 UTC | 2026-07-27 13:12 UTC | 18m |
| TIAWU | TIA | Tobias Bolanos International Airport (MRPV) | Atirro Airport (MRAR) | 2026-07-27 12:53 UTC | 2026-07-27 13:11 UTC | 17m |
| CONGO63 | CON | City Of Colorado Springs Municipal Airport (KCOS) | Usaf Academy Davis Airfield (KAFF) | 2026-07-27 12:57 UTC | 2026-07-27 13:07 UTC | 10m |
| ECLBP | ECL | Braga Municipal Aerodrome (LPBR) | Braga Municipal Aerodrome (LPBR) | 2026-07-27 12:55 UTC | 2026-07-27 13:07 UTC | 12m |
| PAV427 | PAV | Ibiza Airport (LEIB) | Samedan Airport (LSZS) | 2026-07-27 10:12 UTC | 2026-07-27 13:01 UTC | 2h 49m |
| N1323X |  | Trenton Mercer Airport (KTTN) | Sky Manor Airport (KN40) | 2026-07-27 12:43 UTC | 2026-07-27 12:59 UTC | 15m |
| HK2978G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-07-27 12:33 UTC | 2026-07-27 12:55 UTC | 21m |
| GEGCB | GEG | Wethersfield Airport (EGVT) | Wethersfield Airport (EGVT) | 2026-07-27 12:03 UTC | 2026-07-27 12:55 UTC | 52m |
| N24144 |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-07-27 12:27 UTC | 2026-07-27 12:53 UTC | 26m |
| N838WC |  | Provo Municipal Airport (KPVU) | Crystal Springs Ranch Airport (UT54) | 2026-07-27 11:59 UTC | 2026-07-27 12:50 UTC | 51m |
| LJC2 | LJC | Gloucestershire Airport (EGBJ) | Exeter International Airport (EGTE) | 2026-07-27 12:16 UTC | 2026-07-27 12:49 UTC | 32m |
| GRAIL02 | GRA | Ball Airport (5MS8) | Ball Airport (5MS8) | 2026-07-27 12:35 UTC | 2026-07-27 12:48 UTC | 13m |
| N9552A |  | Addison Airport (KADS) | J Ranch Airport (41TX) | 2026-07-27 12:18 UTC | 2026-07-27 12:47 UTC | 28m |
| N529LF |  | Albuquerque International Sunport Airport (KABQ) | Socorro Municipal Airport (KONM) | 2026-07-27 12:09 UTC | 2026-07-27 12:46 UTC | 37m |
| APACHE1 | APA | Gilze Rijen Air Base (EHGR) | Gilze Rijen Air Base (EHGR) | 2026-07-27 12:29 UTC | 2026-07-27 12:46 UTC | 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
