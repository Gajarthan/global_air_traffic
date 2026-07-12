# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--12_08:41:31_UTC-green)

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

**Latest saved flight:** 2026-07-12 08:41:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-12 08:41:31 UTC

- **138,412** saved flights
- **46,653** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **138,412** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,663,055.2 tonnes** estimated CO2 emissions
- **96,409,000 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5636 |
| 2 | SkyWest Airlines | 5076 |
| 3 | EJA | 2714 |
| 4 | IndiGo | 2547 |
| 5 | American Airlines | 2184 |
| 6 | Southwest Airlines | 2088 |
| 7 | ENY | 1736 |
| 8 | Delta Air Lines | 1645 |
| 9 | Lufthansa | 1413 |
| 10 | LATAM Airlines | 1271 |
| 11 | Vueling | 1198 |
| 12 | WIF | 1190 |
| 13 | AZU | 1188 |
| 14 | LXJ | 1061 |
| 15 | AXM | 1039 |
| 16 | Swiss International | 986 |
| 17 | easyJet | 896 |
| 18 | All Nippon Airways | 892 |
| 19 | Alaska Airlines | 874 |
| 20 | QLK | 865 |
| 21 | EJU | 850 |
| 22 | VIV | 760 |
| 23 | AEE | 747 |
| 24 | CXK | 740 |
| 25 | Air France | 739 |
| 26 | United Airlines | 729 |
| 27 | Cathay Pacific | 727 |
| 28 | JetBlue | 727 |
| 29 | MXY | 721 |
| 30 | GLO | 708 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 118872 |
| 2 | 🇪🇸 ES | 9102 |
| 3 | 🇮🇳 IN | 7984 |
| 4 | 🇦🇺 AU | 7914 |
| 5 | 🇧🇷 BR | 7802 |
| 6 | 🇨🇦 CA | 7280 |
| 7 | 🇮🇹 IT | 7231 |
| 8 | 🇩🇪 DE | 7226 |
| 9 | 🇬🇧 GB | 6270 |
| 10 | 🇯🇵 JP | 5841 |
| 11 | 🇫🇷 FR | 5506 |
| 12 | 🇨🇴 CO | 4371 |
| 13 | 🇲🇽 MX | 4013 |
| 14 | 🇬🇷 GR | 3950 |
| 15 | 🇳🇴 NO | 3727 |
| 16 | 🇨🇭 CH | 3589 |
| 17 | 🇹🇷 TR | 3240 |
| 18 | 🇲🇾 MY | 2698 |
| 19 | 🇵🇱 PL | 2319 |
| 20 | 🇿🇦 ZA | 2268 |
| 21 | 🇳🇿 NZ | 2132 |
| 22 | 🇹🇭 TH | 2101 |
| 23 | 🇰🇷 KR | 2000 |
| 24 | 🇵🇭 PH | 1889 |
| 25 | 🇬🇹 GT | 1839 |
| 26 | 🇲🇦 MA | 1457 |
| 27 | 🇲🇪 ME | 1373 |
| 28 | 🇳🇱 NL | 1293 |
| 29 | 🇭🇷 HR | 1256 |
| 30 | 🇲🇴 MO | 1188 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2871 |
| 2 | Denver International Airport |  | US | 2321 |
| 3 | Tokyo International Airport |  | JP | 1900 |
| 4 | Indira Gandhi International Airport |  | IN | 1762 |
| 5 | Harry Reid International Airport |  | US | 1729 |
| 6 | Guaymaral Airport |  | CO | 1684 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1603 |
| 8 | Zurich Airport |  | CH | 1538 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1458 |
| 10 | La Aurora Airport |  | GT | 1421 |
| 11 | Frankfurt am Main International Airport |  | DE | 1368 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1326 |
| 13 | Chicago O'Hare International Airport |  | US | 1306 |
| 14 | El Dorado International Airport |  | CO | 1231 |
| 15 | Salt Lake City International Airport |  | US | 1227 |
| 16 | Macau International Airport |  | MO | 1188 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1187 |
| 18 | Capua Airport |  | IT | 1137 |
| 19 | Madrid Barajas International Airport |  | ES | 1128 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1117 |
| 21 | Congonhas Airport |  | BR | 1113 |
| 22 | Kuala Lumpur International Airport |  | MY | 1046 |
| 23 | Charlotte/Douglas International Airport |  | US | 1013 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 998 |
| 25 | Charles de Gaulle International Airport |  | FR | 983 |
| 26 | Bengaluru International Airport |  | IN | 959 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 953 |
| 28 | Malpensa International Airport |  | IT | 904 |
| 29 | Ninoy Aquino International Airport |  | PH | 879 |
| 30 | Daniel K Inouye International Airport |  | US | 851 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 842 |
| 32 | Barcelona International Airport |  | ES | 842 |
| 33 | Tenerife Norte Airport |  | ES | 813 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 811 |
| 35 | Calgary International Airport |  | CA | 801 |
| 36 | Viracopos International Airport |  | BR | 791 |
| 37 | Scottsdale Airport |  | US | 791 |
| 38 | Seattle-Tacoma International Airport |  | US | 788 |
| 39 | Amsterdam Airport Schiphol |  | NL | 777 |
| 40 | Vitoria/Foronda Airport |  | ES | 775 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 709 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 501 | 21m | 244 km | 2,109.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 341 | 24m | 225 km | 1,322.9 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 340 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 330 | 1h 9m | 770 km | 4,383.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 297 | 14m | 114 km | 582.5 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 258 | 26m | 275 km | 1,222.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 252 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 206 | 22m | 55 km | 195.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 189 | 26m | 215 km | 700.0 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 189 | 44m | 241 km | 785.1 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 187 | 1h 46m | 1,423 km | 4,589.3 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 185 | 20m | 99 km | 316.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 182 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 176 | 27m | 152 km | 460.0 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 174 | 20m | 250 km | 751.6 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 169 | 31m | 369 km | 1,075.7 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 166 | 18m | 144 km | 412.9 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 163 | 44m | 452 km | 1,270.3 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 161 | 1h 16m | 961 km | 2,668.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 159 | 1h 1m | 695 km | 1,905.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 156 | 1h 38m | 1,156 km | 3,112.1 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 155 | 14m | 154 km | 410.7 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 152 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DFALL | DFA | Hildesheim Airport (EDVM) | Hildesheim Airport (EDVM) | 2026-07-12 07:03 UTC | 2026-07-12 08:41 UTC | 1h 37m |
| DMWCM | DMW | Chemnitz/Jahnsdorf Airport (EDCJ) | Grosenhain Airport (EDAK) | 2026-07-12 08:01 UTC | 2026-07-12 08:34 UTC | 33m |
| 5YSKE |  | Jomo Kenyatta International Airport (HKJK) | Jomo Kenyatta International Airport (HKJK) | 2026-07-12 08:18 UTC | 2026-07-12 08:18 UTC | 0m |
| DEGLW | DEG | Wurzburg-Schenkenturm Airport (EDFW) | Wurzburg-Schenkenturm Airport (EDFW) | 2026-07-12 07:40 UTC | 2026-07-12 08:11 UTC | 30m |
| IGO1157 | IndiGo | Juhu Aerodrome (VAJJ) | Langtang Airport (VNLT) | 2026-07-12 06:03 UTC | 2026-07-12 08:08 UTC | 2h 4m |
| VOE1WR | VOE | Bastia-Poretta Airport (LFKB) | Caen-Carpiquet Airport (LFRK) | 2026-07-12 06:23 UTC | 2026-07-12 08:00 UTC | 1h 37m |
| RYR9695 | Ryanair | Copernicus Wrocław Airport (EPWR) | Rijeka Airport (LDRI) | 2026-07-12 06:51 UTC | 2026-07-12 07:52 UTC | 1h 0m |
| AFR38SN | Air France | Charles de Gaulle International Airport (LFPG) | Zurich Airport (LSZH) | 2026-07-12 07:02 UTC | 2026-07-12 07:50 UTC | 48m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-07-12 07:22 UTC | 2026-07-12 07:48 UTC | 26m |
| VLG2SK | Vueling | Barcelona International Airport (LEBL) | Decimomannu Airport (LIED) | 2026-07-12 06:54 UTC | 2026-07-12 07:44 UTC | 49m |
| NJE798V | NJE | Geneva Cointrin International Airport (LSGG) | Samedan Airport (LSZS) | 2026-07-12 06:53 UTC | 2026-07-12 07:42 UTC | 49m |
| RYR69BK | Ryanair | Nantes Atlantique Airport (LFRS) | Marseille Provence Airport (LFML) | 2026-07-12 06:29 UTC | 2026-07-12 07:36 UTC | 1h 7m |
| VOE3DL | VOE | Menorca Airport (LEMH) | Bilbao Airport (LEBB) | 2026-07-12 06:26 UTC | 2026-07-12 07:35 UTC | 1h 9m |
| VJH387 | VJH | Thessaloniki Macedonia International Airport (LGTS) | Mikonos Airport (LGMK) | 2026-07-12 06:44 UTC | 2026-07-12 07:35 UTC | 50m |
| IGO6192 | IndiGo | Juhu Aerodrome (VAJJ) | Pune Airport (VAPO) | 2026-07-12 07:21 UTC | 2026-07-12 07:33 UTC | 11m |
| BHA505 | BHA | Tribhuvan International Airport (VNKT) | Tribhuvan International Airport (VNKT) | 2026-07-12 07:26 UTC | 2026-07-12 07:31 UTC | 5m |
| CEB905 | CEB | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-07-12 07:05 UTC | 2026-07-12 07:30 UTC | 25m |
| VLG66VP | Vueling | Barcelona International Airport (LEBL) | Bilbao Airport (LEBB) | 2026-07-12 06:45 UTC | 2026-07-12 07:29 UTC | 43m |
| NSZ3538 | NSZ | Copenhagen Kastrup Airport (EKCH) | Amsterdam Airport Schiphol (EHAM) | 2026-07-12 06:21 UTC | 2026-07-12 07:25 UTC | 1h 4m |
| N559AJ |  | Sandpoint Airport (KSZT) | 6OR9 (6OR9) | 2026-07-12 06:28 UTC | 2026-07-12 07:25 UTC | 57m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
