# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--21_23:56:44_UTC-green)

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

**Latest saved flight:** 2026-06-21 23:56:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-21 23:56:44 UTC

- **116,947** saved flights
- **40,439** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **116,947** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,420,542.4 tonnes** estimated CO2 emissions
- **82,350,287 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4830 |
| 2 | SkyWest Airlines | 4342 |
| 3 | EJA | 2269 |
| 4 | IndiGo | 2260 |
| 5 | American Airlines | 1825 |
| 6 | Southwest Airlines | 1743 |
| 7 | ENY | 1460 |
| 8 | Delta Air Lines | 1381 |
| 9 | Lufthansa | 1293 |
| 10 | Vueling | 1051 |
| 11 | LATAM Airlines | 1033 |
| 12 | WIF | 1031 |
| 13 | AZU | 973 |
| 14 | AXM | 960 |
| 15 | LXJ | 891 |
| 16 | Swiss International | 826 |
| 17 | All Nippon Airways | 802 |
| 18 | Alaska Airlines | 780 |
| 19 | QLK | 752 |
| 20 | easyJet | 749 |
| 21 | EJU | 732 |
| 22 | Cathay Pacific | 673 |
| 23 | AEE | 657 |
| 24 | VIV | 646 |
| 25 | United Airlines | 644 |
| 26 | Air France | 643 |
| 27 | CXK | 626 |
| 28 | MXY | 620 |
| 29 | AXB | 579 |
| 30 | GLO | 574 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 98845 |
| 2 | 🇪🇸 ES | 7970 |
| 3 | 🇮🇳 IN | 7111 |
| 4 | 🇦🇺 AU | 6896 |
| 5 | 🇧🇷 BR | 6455 |
| 6 | 🇮🇹 IT | 6253 |
| 7 | 🇩🇪 DE | 6232 |
| 8 | 🇨🇦 CA | 6129 |
| 9 | 🇯🇵 JP | 5239 |
| 10 | 🇬🇧 GB | 5111 |
| 11 | 🇫🇷 FR | 4661 |
| 12 | 🇨🇴 CO | 3992 |
| 13 | 🇲🇽 MX | 3440 |
| 14 | 🇬🇷 GR | 3343 |
| 15 | 🇳🇴 NO | 3205 |
| 16 | 🇨🇭 CH | 3001 |
| 17 | 🇲🇾 MY | 2493 |
| 18 | 🇹🇷 TR | 2379 |
| 19 | 🇿🇦 ZA | 1974 |
| 20 | 🇵🇱 PL | 1921 |
| 21 | 🇳🇿 NZ | 1912 |
| 22 | 🇹🇭 TH | 1892 |
| 23 | 🇰🇷 KR | 1890 |
| 24 | 🇵🇭 PH | 1698 |
| 25 | 🇬🇹 GT | 1650 |
| 26 | 🇲🇦 MA | 1271 |
| 27 | 🇲🇴 MO | 1169 |
| 28 | 🇲🇪 ME | 1150 |
| 29 | 🇳🇱 NL | 1126 |
| 30 | 🇭🇷 HR | 1019 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2468 |
| 2 | Denver International Airport |  | US | 1970 |
| 3 | Tokyo International Airport |  | JP | 1736 |
| 4 | Indira Gandhi International Airport |  | IN | 1561 |
| 5 | Guaymaral Airport |  | CO | 1482 |
| 6 | Harry Reid International Airport |  | US | 1460 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1428 |
| 8 | Zurich Airport |  | CH | 1307 |
| 9 | La Aurora Airport |  | GT | 1274 |
| 10 | Frankfurt am Main International Airport |  | DE | 1260 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1244 |
| 12 | El Dorado International Airport |  | CO | 1171 |
| 13 | Macau International Airport |  | MO | 1169 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1162 |
| 15 | Chicago O'Hare International Airport |  | US | 1150 |
| 16 | Capua Airport |  | IT | 1016 |
| 17 | Salt Lake City International Airport |  | US | 1002 |
| 18 | Madrid Barajas International Airport |  | ES | 988 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 978 |
| 20 | Kuala Lumpur International Airport |  | MY | 962 |
| 21 | Congonhas Airport |  | BR | 899 |
| 22 | Charlotte/Douglas International Airport |  | US | 891 |
| 23 | General Edward Lawrence Logan International Airport |  | US | 869 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 866 |
| 25 | Charles de Gaulle International Airport |  | FR | 861 |
| 26 | Bengaluru International Airport |  | IN | 860 |
| 27 | Malpensa International Airport |  | IT | 829 |
| 28 | Ninoy Aquino International Airport |  | PH | 784 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 764 |
| 30 | Daniel K Inouye International Airport |  | US | 760 |
| 31 | Tenerife Norte Airport |  | ES | 758 |
| 32 | Barcelona International Airport |  | ES | 742 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 733 |
| 34 | Calgary International Airport |  | CA | 686 |
| 35 | Don Mueang International Airport |  | TH | 685 |
| 36 | Vitoria/Foronda Airport |  | ES | 685 |
| 37 | Amsterdam Airport Schiphol |  | NL | 683 |
| 38 | Seattle-Tacoma International Airport |  | US | 673 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 668 |
| 40 | Viracopos International Airport |  | BR | 664 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 615 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 424 | 21m | 244 km | 1,785.3 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 313 | 24m | 225 km | 1,214.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 301 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 285 | 1h 25m | 910 km | 4,472.3 t |
| 7 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 281 | 1h 10m | 770 km | 3,732.9 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 261 | 28m | 304 km | 1,368.2 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 231 | 26m | 275 km | 1,094.6 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 230 | 19m | 165 km | 654.2 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 217 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 174 | 22m | 55 km | 165.4 t |
| 14 | Bodø Airport (ENBO) | ENEN (ENEN) | 169 | 13m | - | - |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 169 | 20m | 99 km | 289.5 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 168 | 26m | 215 km | 622.2 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 159 | 27m | 152 km | 415.5 t |
| 18 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 155 | 44m | 241 km | 643.8 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 154 | 31m | 369 km | 980.2 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 21 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 153 | 44m | 452 km | 1,192.4 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 148 | 20m | 250 km | 639.3 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 147 | 18m | 144 km | 365.7 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 145 | 1h 44m | 1,423 km | 3,558.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 139 | 1h 1m | 695 km | 1,666.2 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 136 | 1h 39m | 1,156 km | 2,713.1 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 136 | 13m | - | - |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 133 | 1h 17m | 961 km | 2,204.5 t |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 129 | 24m | 223 km | 496.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N234WL |  | KHTO (KHTO) | Laguardia Airport (KLGA) | 2026-06-21 23:14 UTC | 2026-06-21 23:56 UTC | 42m |
| TKR855 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-06-21 23:19 UTC | 2026-06-21 23:50 UTC | 31m |
| N268Z |  | Palo Alto Airport (KPAO) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-06-21 23:32 UTC | 2026-06-21 23:49 UTC | 16m |
| CXK1041 | CXK | Page Field (KFMY) | Page Field (KFMY) | 2026-06-21 23:39 UTC | 2026-06-21 23:43 UTC | 4m |
| N20DN |  | UT09 (UT09) | Nephi Municipal Airport (KU14) | 2026-06-21 23:10 UTC | 2026-06-21 23:43 UTC | 33m |
| PNC0616 | PNC | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-06-21 23:22 UTC | 2026-06-21 23:41 UTC | 18m |
| T815 |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-06-21 23:00 UTC | 2026-06-21 23:38 UTC | 38m |
| T825 |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-06-21 23:00 UTC | 2026-06-21 23:38 UTC | 38m |
| KAI | KAI | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-06-21 22:32 UTC | 2026-06-21 23:37 UTC | 1h 5m |
| TKR137 | TKR | Mesa Gateway Airport (KIWA) | Chapman Ranch Airstrip (58AZ) | 2026-06-21 23:26 UTC | 2026-06-21 23:37 UTC | 11m |
| N598AT |  | Council Bluffs Municipal Airport (KCBF) | Sedalia Regional Airport (KDMO) | 2026-06-21 22:49 UTC | 2026-06-21 23:37 UTC | 47m |
| N294NG |  | Southfork Airport (23ID) | San Carlos Airport (KSQL) | 2026-06-21 21:33 UTC | 2026-06-21 23:33 UTC | 1h 59m |
| XSN06 | XSN | Truckee-Tahoe Airport (KTRK) | San Carlos Airport (KSQL) | 2026-06-21 22:52 UTC | 2026-06-21 23:32 UTC | 39m |
| N931PA |  | Falcon Field (KFFZ) | 4AZ7 (4AZ7) | 2026-06-21 23:00 UTC | 2026-06-21 23:30 UTC | 30m |
| SNH | SNH | Canberra International Airport (YSCB) | Wee Jasper Airport (YWJS) | 2026-06-21 23:14 UTC | 2026-06-21 23:27 UTC | 12m |
| HUSK98 | HUS | Comox Airport (CYQQ) | Pemberton Airport (CYPS) | 2026-06-21 23:13 UTC | 2026-06-21 23:26 UTC | 12m |
| N302CG |  | Southeast Iowa Regional Airport (KBRL) | Walter Storey Field (LL13) | 2026-06-21 22:33 UTC | 2026-06-21 23:22 UTC | 49m |
| N893AP |  | KHTO (KHTO) | Laguardia Airport (KLGA) | 2026-06-21 22:48 UTC | 2026-06-21 23:22 UTC | 34m |
| TKR41 | TKR | AZ86 (AZ86) | 4AZ7 (4AZ7) | 2026-06-21 23:01 UTC | 2026-06-21 23:22 UTC | 20m |
| N4404J |  | Friday Harbor Airport (KFHR) | Friday Harbor Airport (KFHR) | 2026-06-21 22:23 UTC | 2026-06-21 23:21 UTC | 57m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
