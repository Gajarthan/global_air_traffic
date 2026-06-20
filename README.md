# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--20_13:02:18_UTC-green)

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

**Latest saved flight:** 2026-06-20 13:02:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-20 13:02:18 UTC

- **115,451** saved flights
- **40,012** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **115,451** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,404,155.8 tonnes** estimated CO2 emissions
- **81,400,333 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4765 |
| 2 | SkyWest Airlines | 4295 |
| 3 | EJA | 2238 |
| 4 | IndiGo | 2229 |
| 5 | American Airlines | 1805 |
| 6 | Southwest Airlines | 1717 |
| 7 | ENY | 1435 |
| 8 | Delta Air Lines | 1361 |
| 9 | Lufthansa | 1282 |
| 10 | Vueling | 1041 |
| 11 | WIF | 1023 |
| 12 | LATAM Airlines | 1018 |
| 13 | AZU | 964 |
| 14 | AXM | 953 |
| 15 | LXJ | 876 |
| 16 | Swiss International | 816 |
| 17 | All Nippon Airways | 792 |
| 18 | Alaska Airlines | 776 |
| 19 | QLK | 750 |
| 20 | easyJet | 742 |
| 21 | EJU | 726 |
| 22 | Cathay Pacific | 672 |
| 23 | AEE | 648 |
| 24 | United Airlines | 642 |
| 25 | VIV | 638 |
| 26 | Air France | 634 |
| 27 | CXK | 615 |
| 28 | MXY | 611 |
| 29 | AXB | 565 |
| 30 | GLO | 563 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 97463 |
| 2 | 🇪🇸 ES | 7868 |
| 3 | 🇮🇳 IN | 7027 |
| 4 | 🇦🇺 AU | 6857 |
| 5 | 🇧🇷 BR | 6369 |
| 6 | 🇮🇹 IT | 6185 |
| 7 | 🇩🇪 DE | 6158 |
| 8 | 🇨🇦 CA | 6071 |
| 9 | 🇯🇵 JP | 5185 |
| 10 | 🇬🇧 GB | 5007 |
| 11 | 🇫🇷 FR | 4586 |
| 12 | 🇨🇴 CO | 3976 |
| 13 | 🇲🇽 MX | 3399 |
| 14 | 🇬🇷 GR | 3295 |
| 15 | 🇳🇴 NO | 3184 |
| 16 | 🇨🇭 CH | 2943 |
| 17 | 🇲🇾 MY | 2470 |
| 18 | 🇹🇷 TR | 2334 |
| 19 | 🇿🇦 ZA | 1945 |
| 20 | 🇳🇿 NZ | 1899 |
| 21 | 🇵🇱 PL | 1890 |
| 22 | 🇰🇷 KR | 1882 |
| 23 | 🇹🇭 TH | 1881 |
| 24 | 🇵🇭 PH | 1680 |
| 25 | 🇬🇹 GT | 1634 |
| 26 | 🇲🇦 MA | 1255 |
| 27 | 🇲🇴 MO | 1168 |
| 28 | 🇲🇪 ME | 1139 |
| 29 | 🇳🇱 NL | 1116 |
| 30 | 🇭🇷 HR | 1003 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2440 |
| 2 | Denver International Airport |  | US | 1952 |
| 3 | Tokyo International Airport |  | JP | 1719 |
| 4 | Indira Gandhi International Airport |  | IN | 1539 |
| 5 | Guaymaral Airport |  | CO | 1471 |
| 6 | Harry Reid International Airport |  | US | 1448 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1418 |
| 8 | Zurich Airport |  | CH | 1288 |
| 9 | La Aurora Airport |  | GT | 1261 |
| 10 | Frankfurt am Main International Airport |  | DE | 1252 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1236 |
| 12 | El Dorado International Airport |  | CO | 1170 |
| 13 | Macau International Airport |  | MO | 1168 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1153 |
| 15 | Chicago O'Hare International Airport |  | US | 1134 |
| 16 | Capua Airport |  | IT | 1007 |
| 17 | Salt Lake City International Airport |  | US | 989 |
| 18 | Madrid Barajas International Airport |  | ES | 985 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 966 |
| 20 | Kuala Lumpur International Airport |  | MY | 954 |
| 21 | Charlotte/Douglas International Airport |  | US | 884 |
| 22 | Congonhas Airport |  | BR | 883 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 861 |
| 24 | Bengaluru International Airport |  | IN | 851 |
| 25 | Charles de Gaulle International Airport |  | FR | 846 |
| 26 | General Edward Lawrence Logan International Airport |  | US | 844 |
| 27 | Malpensa International Airport |  | IT | 825 |
| 28 | Ninoy Aquino International Airport |  | PH | 775 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 758 |
| 30 | Daniel K Inouye International Airport |  | US | 752 |
| 31 | Tenerife Norte Airport |  | ES | 751 |
| 32 | Barcelona International Airport |  | ES | 738 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 726 |
| 34 | Don Mueang International Airport |  | TH | 682 |
| 35 | Vitoria/Foronda Airport |  | ES | 679 |
| 36 | Calgary International Airport |  | CA | 678 |
| 37 | Amsterdam Airport Schiphol |  | NL | 678 |
| 38 | Seattle-Tacoma International Airport |  | US | 665 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 660 |
| 40 | Viracopos International Airport |  | BR | 658 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 610 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 418 | 21m | 244 km | 1,760.1 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 309 | 24m | 225 km | 1,198.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 298 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 286 | 1h 7m | 706 km | 3,482.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 283 | 1h 25m | 910 km | 4,440.9 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 275 | 1h 10m | 770 km | 3,653.2 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 231 | 26m | 275 km | 1,094.6 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 227 | 19m | 165 km | 645.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 216 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 173 | 22m | 55 km | 164.4 t |
| 14 | Bodø Airport (ENBO) | ENEN (ENEN) | 169 | 13m | - | - |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 168 | 20m | 99 km | 287.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 167 | 26m | 215 km | 618.5 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 157 | 27m | 152 km | 410.3 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 154 | 31m | 369 km | 980.2 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 152 | 44m | 452 km | 1,184.6 t |
| 21 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 151 | 44m | 241 km | 627.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 147 | 20m | 250 km | 635.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 147 | 18m | 144 km | 365.7 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 139 | 1h 44m | 1,423 km | 3,411.3 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 138 | 1h 1m | 695 km | 1,654.2 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 135 | 1h 39m | 1,156 km | 2,693.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 134 | 13m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 130 | 1h 17m | 961 km | 2,154.8 t |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 129 | 24m | 223 km | 496.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-06-20 12:26 UTC | 2026-06-20 13:02 UTC | 35m |
| SCA18 | SCA | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-06-20 12:22 UTC | 2026-06-20 12:58 UTC | 35m |
| N80866 |  | Albuquerque International Sunport Airport (KABQ) | Socorro Municipal Airport (KONM) | 2026-06-20 12:18 UTC | 2026-06-20 12:50 UTC | 32m |
| JBU162 | JetBlue | Sacramento International Airport (KSMF) | Sharretts Airport (PN91) | 2026-06-20 08:01 UTC | 2026-06-20 12:49 UTC | 4h 48m |
| RISSNGTN | RIS | RAF Brize Norton (EGVN) | RAF Brize Norton (EGVN) | 2026-06-20 12:42 UTC | 2026-06-20 12:49 UTC | 7m |
| N1091M |  | Falcon Field (KFFZ) | Falcon Field (KFFZ) | 2026-06-20 12:19 UTC | 2026-06-20 12:45 UTC | 26m |
| SCX3047 | SCX | Smitty's Landing Airport (1MU2) | Greater Cumberland Regional Airport (KCBE) | 2026-06-20 10:31 UTC | 2026-06-20 12:43 UTC | 2h 11m |
| JBU1285 | JetBlue | General Edward Lawrence Logan International Airport (KBOS) | K5G6 (K5G6) | 2026-06-20 10:52 UTC | 2026-06-20 12:40 UTC | 1h 48m |
| N750VL |  | Miami Homestead General Aviation Airport (KX51) | Miami Homestead General Aviation Airport (KX51) | 2026-06-20 12:24 UTC | 2026-06-20 12:37 UTC | 13m |
| N5121Q |  | Kyle-Oakley Field (KCEY) | Kyle-Oakley Field (KCEY) | 2026-06-20 12:28 UTC | 2026-06-20 12:37 UTC | 9m |
| N104PF |  | Lewis University Airport (KLOT) | 89LL (89LL) | 2026-06-20 12:19 UTC | 2026-06-20 12:34 UTC | 15m |
| N806XA |  | King Fahd International Airport (OEDF) | Al Ahsa Airport (OEAH) | 2026-06-20 12:17 UTC | 2026-06-20 12:30 UTC | 13m |
| EFD2F | EFD | Stuttgart Airport (EDDS) | Graz Airport (LOWG) | 2026-06-20 11:32 UTC | 2026-06-20 12:28 UTC | 56m |
| EJA453 | EJA | Reading Regional/Carl A Spaatz Field (KRDG) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-06-20 12:18 UTC | 2026-06-20 12:28 UTC | 10m |
| NWX813 | NWX | Lebanon Municipal Airport (KM54) | Cedar Crest Field (1TN0) | 2026-06-20 11:39 UTC | 2026-06-20 12:27 UTC | 48m |
| SAS42G | Scandinavian Airlines | Oslo Gardermoen Airport (ENGM) | Trondheim Airport Vaernes (ENVA) | 2026-06-20 11:46 UTC | 2026-06-20 12:26 UTC | 39m |
| ABY131 | ABY | Hamad International Airport (OTHH) | Das Island Airport (OMAS) | 2026-06-20 12:01 UTC | 2026-06-20 12:17 UTC | 15m |
| N998RA |  | Frederick Douglass/Greater Rochester International Airport (KROC) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-06-20 11:47 UTC | 2026-06-20 12:17 UTC | 29m |
| EJM180 | EJM | Catania / Fontanarossa Airport (LICC) | Ibiza Airport (LEIB) | 2026-06-20 10:35 UTC | 2026-06-20 12:16 UTC | 1h 41m |
| TAM3214 | LATAM Airlines | Guarulhos - Governador Andre Franco Montoro International Airport (SBGR) | Fazenda Sao Francisco Airport (SDFN) | 2026-06-20 11:36 UTC | 2026-06-20 12:09 UTC | 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
