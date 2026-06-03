# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--03_22:38:47_UTC-green)

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

**Latest saved flight:** 2026-06-03 22:38:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-03 22:38:47 UTC

- **101,793** saved flights
- **36,077** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **101,793** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,244,843.4 tonnes** estimated CO2 emissions
- **72,164,833 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4199 |
| 2 | SkyWest Airlines | 3824 |
| 3 | IndiGo | 2038 |
| 4 | EJA | 1945 |
| 5 | American Airlines | 1646 |
| 6 | Southwest Airlines | 1543 |
| 7 | ENY | 1264 |
| 8 | Delta Air Lines | 1198 |
| 9 | Lufthansa | 1188 |
| 10 | Vueling | 947 |
| 11 | LATAM Airlines | 901 |
| 12 | WIF | 891 |
| 13 | AXM | 878 |
| 14 | AZU | 822 |
| 15 | LXJ | 765 |
| 16 | Swiss International | 738 |
| 17 | All Nippon Airways | 718 |
| 18 | Alaska Airlines | 714 |
| 19 | QLK | 684 |
| 20 | easyJet | 661 |
| 21 | EJU | 638 |
| 22 | Cathay Pacific | 615 |
| 23 | AEE | 590 |
| 24 | Air France | 587 |
| 25 | VIV | 587 |
| 26 | United Airlines | 568 |
| 27 | MXY | 549 |
| 28 | CXK | 545 |
| 29 | Japan Airlines | 509 |
| 30 | AXB | 501 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 85505 |
| 2 | 🇪🇸 ES | 7027 |
| 3 | 🇮🇳 IN | 6449 |
| 4 | 🇦🇺 AU | 6179 |
| 5 | 🇧🇷 BR | 5567 |
| 6 | 🇩🇪 DE | 5492 |
| 7 | 🇮🇹 IT | 5412 |
| 8 | 🇨🇦 CA | 5280 |
| 9 | 🇯🇵 JP | 4699 |
| 10 | 🇬🇧 GB | 4314 |
| 11 | 🇫🇷 FR | 4048 |
| 12 | 🇨🇴 CO | 3512 |
| 13 | 🇲🇽 MX | 3078 |
| 14 | 🇬🇷 GR | 2894 |
| 15 | 🇳🇴 NO | 2821 |
| 16 | 🇨🇭 CH | 2615 |
| 17 | 🇲🇾 MY | 2240 |
| 18 | 🇹🇷 TR | 1925 |
| 19 | 🇿🇦 ZA | 1769 |
| 20 | 🇳🇿 NZ | 1717 |
| 21 | 🇹🇭 TH | 1690 |
| 22 | 🇰🇷 KR | 1645 |
| 23 | 🇵🇱 PL | 1632 |
| 24 | 🇬🇹 GT | 1501 |
| 25 | 🇵🇭 PH | 1489 |
| 26 | 🇲🇦 MA | 1135 |
| 27 | 🇲🇴 MO | 1074 |
| 28 | 🇳🇱 NL | 1010 |
| 29 | 🇲🇪 ME | 961 |
| 30 | 🇭🇷 HR | 900 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2210 |
| 2 | Denver International Airport |  | US | 1743 |
| 3 | Tokyo International Airport |  | JP | 1557 |
| 4 | Indira Gandhi International Airport |  | IN | 1403 |
| 5 | Harry Reid International Airport |  | US | 1308 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1301 |
| 7 | Guaymaral Airport |  | CO | 1268 |
| 8 | Frankfurt am Main International Airport |  | DE | 1188 |
| 9 | Zurich Airport |  | CH | 1165 |
| 10 | La Aurora Airport |  | GT | 1154 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1100 |
| 12 | El Dorado International Airport |  | CO | 1077 |
| 13 | Macau International Airport |  | MO | 1074 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1034 |
| 15 | Chicago O'Hare International Airport |  | US | 1019 |
| 16 | Madrid Barajas International Airport |  | ES | 887 |
| 17 | Kuala Lumpur International Airport |  | MY | 885 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 876 |
| 19 | Salt Lake City International Airport |  | US | 860 |
| 20 | Capua Airport |  | IT | 844 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 793 |
| 22 | Charlotte/Douglas International Airport |  | US | 788 |
| 23 | Charles de Gaulle International Airport |  | FR | 780 |
| 24 | Malpensa International Airport |  | IT | 771 |
| 25 | Congonhas Airport |  | BR | 771 |
| 26 | Bengaluru International Airport |  | IN | 770 |
| 27 | Daniel K Inouye International Airport |  | US | 705 |
| 28 | Tenerife Norte Airport |  | ES | 699 |
| 29 | Ninoy Aquino International Airport |  | PH | 681 |
| 30 | Barcelona International Airport |  | ES | 672 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 663 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 661 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 649 |
| 34 | Amsterdam Airport Schiphol |  | NL | 624 |
| 35 | Don Mueang International Airport |  | TH | 618 |
| 36 | Vitoria/Foronda Airport |  | ES | 616 |
| 37 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 38 | Calgary International Airport |  | CA | 599 |
| 39 | Seattle-Tacoma International Airport |  | US | 590 |
| 40 | John Paul II International Airport Kraków-Balice Airport |  | PL | 575 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 522 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 374 | 21m | 244 km | 1,574.8 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 279 | 1h 7m | 706 km | 3,396.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 271 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 268 | 24m | 225 km | 1,039.7 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 256 | 14m | 114 km | 502.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 249 | 1h 26m | 910 km | 3,907.4 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 246 | 28m | 304 km | 1,289.6 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 233 | 1h 10m | 770 km | 3,095.2 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 214 | 19m | 165 km | 608.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 201 | 26m | 275 km | 952.5 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 159 | 20m | 99 km | 272.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 153 | 22m | 55 km | 145.4 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 150 | 27m | 215 km | 555.5 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 147 | 14m | 154 km | 389.5 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 143 | 44m | 452 km | 1,114.5 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 143 | 31m | 369 km | 910.2 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 141 | 27m | 152 km | 368.5 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 136 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 134 | 20m | 250 km | 578.8 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 131 | 20m | 147 km | 331.5 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 131 | 18m | 144 km | 325.9 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 128 | 1h 39m | 1,156 km | 2,553.6 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 127 | 1h 1m | 695 km | 1,522.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 120 | 1h 43m | 1,423 km | 2,945.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 118 | 1h 18m | 961 km | 1,955.9 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 117 | 12m | - | - |
| 30 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N9994V |  | Hudson Valley Regional Airport (KPOU) | Hudson Valley Regional Airport (KPOU) | 2026-06-03 21:56 UTC | 2026-06-03 22:38 UTC | 42m |
| N285KT |  | Joe Foss Field (KFSD) | Mitchell Municipal Airport (KMHE) | 2026-06-03 22:04 UTC | 2026-06-03 22:37 UTC | 33m |
| YTJ | YTJ | Toowoomba Wellcamp Airport (YBWW) | Sunshine Coast Airport (YBMC) | 2026-06-03 21:29 UTC | 2026-06-03 22:21 UTC | 52m |
| N5217H |  | Wadsworth Municipal Airport (K3G3) | Wadsworth Municipal Airport (K3G3) | 2026-06-03 21:56 UTC | 2026-06-03 22:20 UTC | 23m |
| EJA874 | EJA | San Diego International Airport (KSAN) | Borrego Valley Airport (KL08) | 2026-06-03 21:55 UTC | 2026-06-03 22:10 UTC | 15m |
| N979TM |  | Redding Regional Airport (KRDD) | North Las Vegas Airport (KVGT) | 2026-06-03 21:06 UTC | 2026-06-03 22:07 UTC | 1h 0m |
| N424KT |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-06-03 21:36 UTC | 2026-06-03 22:06 UTC | 29m |
| N185FK |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-06-03 21:36 UTC | 2026-06-03 22:05 UTC | 28m |
| N114UV |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-06-03 21:47 UTC | 2026-06-03 22:04 UTC | 17m |
| N565TA |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-06-03 21:38 UTC | 2026-06-03 22:01 UTC | 23m |
| KFB510 | KFB | John Wayne/Orange County Airport (KSNA) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-06-03 17:01 UTC | 2026-06-03 22:00 UTC | 4h 59m |
| EJA449 | EJA | Peterborough Airport (CYPQ) | Oakland County International Airport (KPTK) | 2026-06-03 21:12 UTC | 2026-06-03 22:00 UTC | 48m |
| N100BW |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-06-03 21:32 UTC | 2026-06-03 21:59 UTC | 26m |
| ENY3980 | ENY | Chicago O'Hare International Airport (KORD) | Detroit Metro Wayne County Airport (KDTW) | 2026-06-03 21:13 UTC | 2026-06-03 21:58 UTC | 45m |
| N144AL |  | Mineral Wells Regional Airport (KMWL) | Barstow-Daggett Airport (KDAG) | 2026-06-03 19:25 UTC | 2026-06-03 21:58 UTC | 2h 32m |
| N737TX |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Tracy Municipal Airport (KTCY) | 2026-06-03 20:29 UTC | 2026-06-03 21:58 UTC | 1h 29m |
| N263BA |  | Sahoma Lake Airport (03OK) | Granby-Grand County Airport (KGNB) | 2026-06-03 19:59 UTC | 2026-06-03 21:57 UTC | 1h 57m |
| N947VA |  | Oakland/Troy Airport (KVLL) | Oakland/Troy Airport (KVLL) | 2026-06-03 20:50 UTC | 2026-06-03 21:57 UTC | 1h 6m |
| N423BB |  | Aurora State Airport (KUAO) | Chiloquin State Airport (K2S7) | 2026-06-03 21:24 UTC | 2026-06-03 21:54 UTC | 30m |
| N607SA |  | Sacramento Executive Airport (KSAC) | Placerville Airport (KPVF) | 2026-06-03 21:35 UTC | 2026-06-03 21:54 UTC | 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
