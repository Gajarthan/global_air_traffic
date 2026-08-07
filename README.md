# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--07_16:12:50_UTC-green)

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

**Latest saved flight:** 2026-08-07 16:12:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-07 16:12:50 UTC

- **175,715** saved flights
- **56,718** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **175,715** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,113,582.1 tonnes** estimated CO2 emissions
- **122,526,498 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6970 |
| 2 | SkyWest Airlines | 6396 |
| 3 | EJA | 3465 |
| 4 | IndiGo | 3087 |
| 5 | Southwest Airlines | 2761 |
| 6 | American Airlines | 2739 |
| 7 | ENY | 2181 |
| 8 | Delta Air Lines | 2078 |
| 9 | LATAM Airlines | 1626 |
| 10 | Lufthansa | 1583 |
| 11 | AZU | 1558 |
| 12 | WIF | 1475 |
| 13 | Vueling | 1448 |
| 14 | LXJ | 1375 |
| 15 | Swiss International | 1199 |
| 16 | AXM | 1196 |
| 17 | easyJet | 1193 |
| 18 | QLK | 1082 |
| 19 | EJU | 1075 |
| 20 | All Nippon Airways | 1069 |
| 21 | Alaska Airlines | 1065 |
| 22 | VIV | 964 |
| 23 | Cathay Pacific | 944 |
| 24 | CXK | 932 |
| 25 | GLO | 922 |
| 26 | AEE | 916 |
| 27 | United Airlines | 908 |
| 28 | Air France | 906 |
| 29 | MXY | 883 |
| 30 | JetBlue | 869 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 150905 |
| 2 | 🇪🇸 ES | 11254 |
| 3 | 🇧🇷 BR | 10001 |
| 4 | 🇦🇺 AU | 9951 |
| 5 | 🇮🇳 IN | 9676 |
| 6 | 🇨🇦 CA | 9602 |
| 7 | 🇮🇹 IT | 9078 |
| 8 | 🇩🇪 DE | 8721 |
| 9 | 🇬🇧 GB | 8144 |
| 10 | 🇯🇵 JP | 7076 |
| 11 | 🇫🇷 FR | 6990 |
| 12 | 🇨🇴 CO | 6453 |
| 13 | 🇬🇷 GR | 5122 |
| 14 | 🇲🇽 MX | 5019 |
| 15 | 🇨🇭 CH | 4666 |
| 16 | 🇳🇴 NO | 4586 |
| 17 | 🇹🇷 TR | 4338 |
| 18 | 🇲🇾 MY | 3120 |
| 19 | 🇵🇱 PL | 2929 |
| 20 | 🇿🇦 ZA | 2868 |
| 21 | 🇹🇭 TH | 2623 |
| 22 | 🇳🇿 NZ | 2555 |
| 23 | 🇵🇭 PH | 2326 |
| 24 | 🇬🇹 GT | 2239 |
| 25 | 🇰🇷 KR | 2203 |
| 26 | 🇲🇦 MA | 1774 |
| 27 | 🇭🇷 HR | 1717 |
| 28 | 🇲🇪 ME | 1605 |
| 29 | 🇳🇱 NL | 1587 |
| 30 | 🇲🇴 MO | 1507 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3619 |
| 2 | Denver International Airport |  | US | 2895 |
| 3 | Tokyo International Airport |  | JP | 2208 |
| 4 | Guaymaral Airport |  | CO | 2164 |
| 5 | Indira Gandhi International Airport |  | IN | 2148 |
| 6 | Harry Reid International Airport |  | US | 2094 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1908 |
| 8 | Zurich Airport |  | CH | 1867 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1836 |
| 10 | La Aurora Airport |  | GT | 1722 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1607 |
| 12 | El Dorado International Airport |  | CO | 1581 |
| 13 | Chicago O'Hare International Airport |  | US | 1578 |
| 14 | Salt Lake City International Airport |  | US | 1565 |
| 15 | Frankfurt am Main International Airport |  | DE | 1548 |
| 16 | Macau International Airport |  | MO | 1507 |
| 17 | Congonhas Airport |  | BR | 1444 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1424 |
| 19 | Capua Airport |  | IT | 1372 |
| 20 | Madrid Barajas International Airport |  | ES | 1370 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1309 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1237 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1235 |
| 24 | Charlotte/Douglas International Airport |  | US | 1200 |
| 25 | Malpensa International Airport |  | IT | 1195 |
| 26 | Charles de Gaulle International Airport |  | FR | 1195 |
| 27 | Kuala Lumpur International Airport |  | MY | 1175 |
| 28 | Bengaluru International Airport |  | IN | 1151 |
| 29 | Ninoy Aquino International Airport |  | PH | 1094 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1085 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1084 |
| 32 | Barcelona International Airport |  | ES | 1041 |
| 33 | Daniel K Inouye International Airport |  | US | 1010 |
| 34 | Seattle-Tacoma International Airport |  | US | 1009 |
| 35 | Viracopos International Airport |  | BR | 1000 |
| 36 | Reno/Tahoe International Airport |  | US | 994 |
| 37 | Calgary International Airport |  | CA | 994 |
| 38 | Oslo Gardermoen Airport |  | NO | 981 |
| 39 | Tenerife Norte Airport |  | ES | 968 |
| 40 | Amsterdam Airport Schiphol |  | NL | 954 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 895 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 641 | 21m | 244 km | 2,699.1 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 414 | 24m | 225 km | 1,606.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 409 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 406 | 1h 8m | 770 km | 5,393.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 325 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 295 | 27m | 275 km | 1,397.9 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 267 | 44m | 241 km | 1,109.1 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 265 | 22m | 55 km | 251.9 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 242 | 1h 48m | 1,423 km | 5,939.1 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 230 | 20m | 250 km | 993.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 224 | 26m | 215 km | 829.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 224 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 216 | 20m | 99 km | 370.0 t |
| 21 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 211 | 8m | - | - |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 211 | 51m | 556 km | 2,022.6 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 209 | 19m | 144 km | 519.9 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 208 | 1h 15m | 961 km | 3,447.7 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 205 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 204 | 1h 38m | 1,156 km | 4,069.7 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 203 | 31m | 369 km | 1,292.1 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 200 | 24m | 218 km | 753.5 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 200 | 28m | 152 km | 522.7 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 191 | 43m | 452 km | 1,488.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N1420P |  | 61CA (61CA) | Lake Havasu City Airport (KHII) | 2026-08-07 15:30 UTC | 2026-08-07 16:12 UTC | 42m |
| N5173V |  | 2KY1 (2KY1) | Stuart Powell Field (KDVK) | 2026-08-07 15:52 UTC | 2026-08-07 16:08 UTC | 15m |
|  |  | Bellingham International Airport (KBLI) | William R Fairchild International Airport (KCLM) | 2026-08-07 15:43 UTC | 2026-08-07 16:02 UTC | 19m |
| FHRIV | FHR | Rennes-Saint-Jacques Airport (LFRN) | Rennes-Saint-Jacques Airport (LFRN) | 2026-08-07 15:47 UTC | 2026-08-07 16:01 UTC | 13m |
| NIT238 | NIT | Heart Of Georgia Regional Airport (KEZM) | W H 'Bud' Barron Airport (KDBN) | 2026-08-07 15:12 UTC | 2026-08-07 16:00 UTC | 48m |
| CONGO63 | CON | Usaf Academy Davis Airfield (KAFF) | Usaf Academy Davis Airfield (KAFF) | 2026-08-07 14:39 UTC | 2026-08-07 16:00 UTC | 1h 20m |
| LOST56 | LOS | Los Alamitos Army Air Field (KSLI) | Lake Tahoe Airport (KTVL) | 2026-08-07 14:52 UTC | 2026-08-07 15:58 UTC | 1h 5m |
| N407AP |  | Alpine County Airport (KM45) | Alpine County Airport (KM45) | 2026-08-07 15:16 UTC | 2026-08-07 15:54 UTC | 37m |
| NDU30M | NDU | Hillsboro Municipal Airport (K3H4) | Deck Airport (5ND9) | 2026-08-07 15:49 UTC | 2026-08-07 15:52 UTC | 2m |
| N61606 |  | Mckinney Ntl Airport (KTKI) | Mckinney Ntl Airport (KTKI) | 2026-08-07 15:46 UTC | 2026-08-07 15:50 UTC | 4m |
| N107UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-08-07 14:39 UTC | 2026-08-07 15:50 UTC | 1h 10m |
| RATLR09 | RAT | Freeman Ranch Airport (8TX2) | Kimble County Airport (KJCT) | 2026-08-07 15:40 UTC | 2026-08-07 15:50 UTC | 10m |
| N642PF |  | Brandywine Regional Airport (KOQN) | Brandywine Regional Airport (KOQN) | 2026-08-07 15:32 UTC | 2026-08-07 15:49 UTC | 17m |
| RANGR41 | RAN | Lakefront Airport (KNEW) | Maks Army Air Field (KPOE) | 2026-08-07 14:38 UTC | 2026-08-07 15:47 UTC | 1h 9m |
| N7084Y |  | Jonesboro Municipal Airport (KJBR) | Jonesboro Municipal Airport (KJBR) | 2026-08-07 15:29 UTC | 2026-08-07 15:42 UTC | 12m |
| N4036R |  | St Elmo Airport (K2R5) | St Elmo Airport (K2R5) | 2026-08-07 15:35 UTC | 2026-08-07 15:40 UTC | 4m |
| N402ER |  | AZ86 (AZ86) | 42AZ (42AZ) | 2026-08-07 14:47 UTC | 2026-08-07 15:40 UTC | 52m |
| YROPN | YRO | Mikonos Airport (LGMK) | Mikonos Airport (LGMK) | 2026-08-07 15:36 UTC | 2026-08-07 15:39 UTC | 2m |
| N802VA |  | Willows/Glenn County Airport (KWLW) | Willows/Glenn County Airport (KWLW) | 2026-08-07 12:43 UTC | 2026-08-07 15:39 UTC | 2h 55m |
| N786MM |  | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-08-07 15:36 UTC | 2026-08-07 15:37 UTC | 1m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
