# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--02_15:03:16_UTC-green)

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

**Latest saved flight:** 2026-06-02 15:03:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-02 15:03:16 UTC

- **100,966** saved flights
- **35,815** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **100,966** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,235,479.3 tonnes** estimated CO2 emissions
- **71,621,987 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4176 |
| 2 | SkyWest Airlines | 3793 |
| 3 | IndiGo | 2036 |
| 4 | EJA | 1924 |
| 5 | American Airlines | 1631 |
| 6 | Southwest Airlines | 1529 |
| 7 | ENY | 1259 |
| 8 | Delta Air Lines | 1186 |
| 9 | Lufthansa | 1184 |
| 10 | Vueling | 944 |
| 11 | LATAM Airlines | 897 |
| 12 | WIF | 887 |
| 13 | AXM | 871 |
| 14 | AZU | 812 |
| 15 | LXJ | 761 |
| 16 | Swiss International | 736 |
| 17 | All Nippon Airways | 717 |
| 18 | Alaska Airlines | 704 |
| 19 | QLK | 678 |
| 20 | easyJet | 657 |
| 21 | EJU | 635 |
| 22 | Cathay Pacific | 605 |
| 23 | AEE | 589 |
| 24 | Air France | 585 |
| 25 | VIV | 583 |
| 26 | United Airlines | 565 |
| 27 | CXK | 542 |
| 28 | MXY | 541 |
| 29 | Japan Airlines | 509 |
| 30 | AXB | 500 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 84585 |
| 2 | 🇪🇸 ES | 6999 |
| 3 | 🇮🇳 IN | 6439 |
| 4 | 🇦🇺 AU | 6105 |
| 5 | 🇧🇷 BR | 5512 |
| 6 | 🇩🇪 DE | 5468 |
| 7 | 🇮🇹 IT | 5388 |
| 8 | 🇨🇦 CA | 5213 |
| 9 | 🇯🇵 JP | 4687 |
| 10 | 🇬🇧 GB | 4293 |
| 11 | 🇫🇷 FR | 4032 |
| 12 | 🇨🇴 CO | 3497 |
| 13 | 🇲🇽 MX | 3052 |
| 14 | 🇬🇷 GR | 2876 |
| 15 | 🇳🇴 NO | 2811 |
| 16 | 🇨🇭 CH | 2604 |
| 17 | 🇲🇾 MY | 2219 |
| 18 | 🇹🇷 TR | 1918 |
| 19 | 🇿🇦 ZA | 1765 |
| 20 | 🇳🇿 NZ | 1693 |
| 21 | 🇹🇭 TH | 1679 |
| 22 | 🇰🇷 KR | 1639 |
| 23 | 🇵🇱 PL | 1623 |
| 24 | 🇬🇹 GT | 1496 |
| 25 | 🇵🇭 PH | 1473 |
| 26 | 🇲🇦 MA | 1131 |
| 27 | 🇲🇴 MO | 1066 |
| 28 | 🇳🇱 NL | 1007 |
| 29 | 🇲🇪 ME | 960 |
| 30 | 🇭🇷 HR | 892 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2201 |
| 2 | Denver International Airport |  | US | 1734 |
| 3 | Tokyo International Airport |  | JP | 1556 |
| 4 | Indira Gandhi International Airport |  | IN | 1401 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1296 |
| 6 | Harry Reid International Airport |  | US | 1289 |
| 7 | Guaymaral Airport |  | CO | 1264 |
| 8 | Frankfurt am Main International Airport |  | DE | 1184 |
| 9 | Zurich Airport |  | CH | 1155 |
| 10 | La Aurora Airport |  | GT | 1151 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1092 |
| 12 | El Dorado International Airport |  | CO | 1074 |
| 13 | Macau International Airport |  | MO | 1066 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1022 |
| 15 | Chicago O'Hare International Airport |  | US | 1012 |
| 16 | Madrid Barajas International Airport |  | ES | 880 |
| 17 | Kuala Lumpur International Airport |  | MY | 878 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 868 |
| 19 | Salt Lake City International Airport |  | US | 854 |
| 20 | Capua Airport |  | IT | 837 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 784 |
| 22 | Charlotte/Douglas International Airport |  | US | 784 |
| 23 | Charles de Gaulle International Airport |  | FR | 777 |
| 24 | Bengaluru International Airport |  | IN | 769 |
| 25 | Malpensa International Airport |  | IT | 768 |
| 26 | Congonhas Airport |  | BR | 766 |
| 27 | Daniel K Inouye International Airport |  | US | 697 |
| 28 | Tenerife Norte Airport |  | ES | 697 |
| 29 | Ninoy Aquino International Airport |  | PH | 673 |
| 30 | Barcelona International Airport |  | ES | 669 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 658 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 657 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 644 |
| 34 | Amsterdam Airport Schiphol |  | NL | 622 |
| 35 | Don Mueang International Airport |  | TH | 616 |
| 36 | Vitoria/Foronda Airport |  | ES | 614 |
| 37 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 38 | Calgary International Airport |  | CA | 590 |
| 39 | Seattle-Tacoma International Airport |  | US | 580 |
| 40 | John Paul II International Airport Kraków-Balice Airport |  | PL | 574 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 521 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 366 | 21m | 244 km | 1,541.1 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 279 | 1h 7m | 706 km | 3,396.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 271 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 265 | 24m | 225 km | 1,028.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 256 | 14m | 114 km | 502.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 248 | 1h 26m | 910 km | 3,891.7 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 244 | 28m | 304 km | 1,279.1 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 233 | 1h 10m | 770 km | 3,095.2 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 211 | 19m | 165 km | 600.2 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 199 | 26m | 275 km | 943.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 157 | 20m | 99 km | 268.9 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 149 | 27m | 215 km | 551.8 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 146 | 14m | 154 km | 386.8 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 146 | 22m | 55 km | 138.8 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 143 | 44m | 452 km | 1,114.5 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 141 | 31m | 369 km | 897.5 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 141 | 27m | 152 km | 368.5 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 135 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 134 | 20m | 250 km | 578.8 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 130 | 20m | 147 km | 329.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 130 | 18m | 144 km | 323.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 128 | 1h 39m | 1,156 km | 2,553.6 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 127 | 1h 1m | 695 km | 1,522.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 119 | 1h 43m | 1,423 km | 2,920.4 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 117 | 1h 18m | 961 km | 1,939.3 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 117 | 12m | - | - |
| 30 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N408GG |  | Linden Airport (KLDJ) | Newark Liberty International Airport (KEWR) | 2026-06-02 13:48 UTC | 2026-06-02 15:03 UTC | 1h 14m |
| N1154G |  | Boire Field (KASH) | Perrotti Skyranch Airfield (09ME) | 2026-06-02 14:30 UTC | 2026-06-02 15:00 UTC | 30m |
| CCA908 | Air China | Madrid Barajas International Airport (LEMD) | Smolensk North Airport (XUBS) | 2026-06-02 11:40 UTC | 2026-06-02 14:57 UTC | 3h 17m |
| N133PS |  | Waukesha County Airport (KUES) | Sss Aerodrome (WI62) | 2026-06-02 14:41 UTC | 2026-06-02 14:55 UTC | 13m |
| PAT341 | PAT | Patrick Leahy Burlington International Airport (KBTV) | Rhode Island Tf Green International Airport (KPVD) | 2026-06-02 14:05 UTC | 2026-06-02 14:54 UTC | 48m |
| FDL57 | FDL | Republic Airport (KFRG) | Chester Airport (KSNC) | 2026-06-02 14:01 UTC | 2026-06-02 14:51 UTC | 50m |
| DFL5710 | DFL | Vaxjo Kronoberg Airport (ESMX) | Stockholm-Bromma Airport (ESSB) | 2026-06-02 13:49 UTC | 2026-06-02 14:49 UTC | 1h 0m |
| N3576X |  | Square Air Airport (TS63) | Grove Hill Airport (5TX2) | 2026-06-02 14:32 UTC | 2026-06-02 14:46 UTC | 13m |
| N420FJ |  | Rocky Mountain Metro Airport (KBJC) | 51CO (51CO) | 2026-06-02 14:10 UTC | 2026-06-02 14:45 UTC | 35m |
| DLH1455 | Lufthansa | Tirana International Airport Mother Teresa (LATI) | Bad Windsheim Airport (EDQB) | 2026-06-02 12:44 UTC | 2026-06-02 14:45 UTC | 2h 0m |
| DLH5NF | Lufthansa | Munich International Airport (EDDM) | Wasserkuppe Airport (EDER) | 2026-06-02 13:53 UTC | 2026-06-02 14:45 UTC | 51m |
| DLH6LN | Lufthansa | Munich International Airport (EDDM) | Attendorn-Finnentrop Airport (EDKU) | 2026-06-02 13:39 UTC | 2026-06-02 14:45 UTC | 1h 5m |
| DLH8VR | Lufthansa | Copenhagen Kastrup Airport (EKCH) | Gelnhausen Airport (EDFG) | 2026-06-02 13:16 UTC | 2026-06-02 14:45 UTC | 1h 28m |
| KLM20J | KLM Royal Dutch | John Paul II International Airport Kraków-Balice Airport (EPKK) | Twenthe Airport (EHTW) | 2026-06-02 13:02 UTC | 2026-06-02 14:45 UTC | 1h 42m |
| KLM92Y | KLM Royal Dutch | Eleftherios Venizelos International Airport (LGAV) | Hamm-Lippewiesen Airport (EDLH) | 2026-06-02 11:41 UTC | 2026-06-02 14:45 UTC | 3h 3m |
| LHX27W | LHX | Charles de Gaulle International Airport (LFPG) | Dinkelsbuhl-Sinbronn Airport (EDND) | 2026-06-02 13:30 UTC | 2026-06-02 14:45 UTC | 1h 14m |
| RYR59SQ | Ryanair | Palma De Mallorca Airport (LEPA) | Leverkusen Airport (EDKL) | 2026-06-02 12:19 UTC | 2026-06-02 14:45 UTC | 2h 25m |
| AFL1886 | AFL | Sheremetyevo International Airport (UUEE) | Bezymyanka Airfield (UWWG) | 2026-06-02 06:34 UTC | 2026-06-02 14:43 UTC | 8h 8m |
| N2038Q |  | Dean Airport (69TA) | Rabb Dusting Inc Airport (XS66) | 2026-06-02 14:35 UTC | 2026-06-02 14:42 UTC | 7m |
| N475RC |  | Rimrock Airport (48AZ) | Payson Airport (KPAN) | 2026-06-02 14:20 UTC | 2026-06-02 14:41 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
