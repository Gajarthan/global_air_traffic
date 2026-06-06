# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_11:50:30_UTC-green)

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

**Latest saved flight:** 2026-06-06 11:50:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-06 11:50:30 UTC

- **103,691** saved flights
- **36,641** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **103,691** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,267,785.2 tonnes** estimated CO2 emissions
- **73,494,794 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4254 |
| 2 | SkyWest Airlines | 3898 |
| 3 | IndiGo | 2075 |
| 4 | EJA | 1983 |
| 5 | American Airlines | 1675 |
| 6 | Southwest Airlines | 1566 |
| 7 | ENY | 1289 |
| 8 | Delta Air Lines | 1226 |
| 9 | Lufthansa | 1194 |
| 10 | Vueling | 959 |
| 11 | LATAM Airlines | 917 |
| 12 | WIF | 912 |
| 13 | AXM | 896 |
| 14 | AZU | 830 |
| 15 | LXJ | 782 |
| 16 | Swiss International | 747 |
| 17 | All Nippon Airways | 733 |
| 18 | Alaska Airlines | 723 |
| 19 | QLK | 697 |
| 20 | easyJet | 672 |
| 21 | EJU | 648 |
| 22 | Cathay Pacific | 620 |
| 23 | AEE | 601 |
| 24 | Air France | 594 |
| 25 | VIV | 594 |
| 26 | United Airlines | 574 |
| 27 | MXY | 560 |
| 28 | CXK | 554 |
| 29 | Japan Airlines | 522 |
| 30 | AXB | 510 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 87168 |
| 2 | 🇪🇸 ES | 7132 |
| 3 | 🇮🇳 IN | 6552 |
| 4 | 🇦🇺 AU | 6308 |
| 5 | 🇧🇷 BR | 5655 |
| 6 | 🇩🇪 DE | 5573 |
| 7 | 🇮🇹 IT | 5499 |
| 8 | 🇨🇦 CA | 5394 |
| 9 | 🇯🇵 JP | 4816 |
| 10 | 🇬🇧 GB | 4369 |
| 11 | 🇫🇷 FR | 4109 |
| 12 | 🇨🇴 CO | 3554 |
| 13 | 🇲🇽 MX | 3110 |
| 14 | 🇬🇷 GR | 2948 |
| 15 | 🇳🇴 NO | 2886 |
| 16 | 🇨🇭 CH | 2653 |
| 17 | 🇲🇾 MY | 2293 |
| 18 | 🇹🇷 TR | 1967 |
| 19 | 🇿🇦 ZA | 1800 |
| 20 | 🇳🇿 NZ | 1742 |
| 21 | 🇹🇭 TH | 1722 |
| 22 | 🇰🇷 KR | 1721 |
| 23 | 🇵🇱 PL | 1664 |
| 24 | 🇵🇭 PH | 1530 |
| 25 | 🇬🇹 GT | 1509 |
| 26 | 🇲🇦 MA | 1141 |
| 27 | 🇲🇴 MO | 1092 |
| 28 | 🇳🇱 NL | 1020 |
| 29 | 🇲🇪 ME | 981 |
| 30 | 🇭🇷 HR | 909 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2255 |
| 2 | Denver International Airport |  | US | 1776 |
| 3 | Tokyo International Airport |  | JP | 1599 |
| 4 | Indira Gandhi International Airport |  | IN | 1422 |
| 5 | Harry Reid International Airport |  | US | 1331 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1320 |
| 7 | Guaymaral Airport |  | CO | 1287 |
| 8 | Frankfurt am Main International Airport |  | DE | 1193 |
| 9 | Zurich Airport |  | CH | 1177 |
| 10 | La Aurora Airport |  | GT | 1162 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1120 |
| 12 | Macau International Airport |  | MO | 1092 |
| 13 | El Dorado International Airport |  | CO | 1089 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1051 |
| 15 | Chicago O'Hare International Airport |  | US | 1038 |
| 16 | Madrid Barajas International Airport |  | ES | 902 |
| 17 | Kuala Lumpur International Airport |  | MY | 897 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 888 |
| 19 | Salt Lake City International Airport |  | US | 878 |
| 20 | Capua Airport |  | IT | 862 |
| 21 | Charlotte/Douglas International Airport |  | US | 807 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 803 |
| 23 | Charles de Gaulle International Airport |  | FR | 789 |
| 24 | Congonhas Airport |  | BR | 786 |
| 25 | Bengaluru International Airport |  | IN | 785 |
| 26 | Malpensa International Airport |  | IT | 779 |
| 27 | Daniel K Inouye International Airport |  | US | 712 |
| 28 | Tenerife Norte Airport |  | ES | 706 |
| 29 | Ninoy Aquino International Airport |  | PH | 698 |
| 30 | Barcelona International Airport |  | ES | 682 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 672 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 668 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 662 |
| 34 | Amsterdam Airport Schiphol |  | NL | 631 |
| 35 | Don Mueang International Airport |  | TH | 630 |
| 36 | Vitoria/Foronda Airport |  | ES | 623 |
| 37 | Calgary International Airport |  | CA | 616 |
| 38 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 39 | Seattle-Tacoma International Airport |  | US | 600 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 590 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 531 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 380 | 21m | 244 km | 1,600.1 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 280 | 1h 7m | 706 km | 3,409.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 276 | 24m | 225 km | 1,070.7 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 273 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 258 | 14m | 114 km | 506.0 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 257 | 1h 25m | 910 km | 4,032.9 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 256 | 28m | 304 km | 1,342.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 241 | 1h 10m | 770 km | 3,201.5 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 216 | 19m | 165 km | 614.4 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 204 | 26m | 275 km | 966.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 159 | 20m | 99 km | 272.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 152 | 27m | 215 km | 562.9 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 147 | 14m | 154 km | 389.5 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 144 | 44m | 452 km | 1,122.3 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 144 | 31m | 369 km | 916.6 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 144 | 27m | 152 km | 376.3 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 139 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 134 | 18m | 144 km | 333.3 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 128 | 1h 1m | 695 km | 1,534.3 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 121 | 1h 43m | 1,423 km | 2,969.5 t |
| 28 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 119 | 44m | 241 km | 494.3 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 119 | 1h 52m | 1,304 km | 2,677.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 118 | 1h 18m | 961 km | 1,955.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AFR34MZ | Air France | Charles de Gaulle International Airport (LFPG) | Zurich Airport (LSZH) | 2026-06-06 11:03 UTC | 2026-06-06 11:50 UTC | 47m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-06-06 11:30 UTC | 2026-06-06 11:40 UTC | 10m |
| MBIGG | MBI | Geneva Cointrin International Airport (LSGG) | Nice-Cote d'Azur Airport (LFMN) | 2026-06-06 10:47 UTC | 2026-06-06 11:39 UTC | 51m |
| N247EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-06-06 10:45 UTC | 2026-06-06 11:39 UTC | 54m |
| N4026E |  | Donalsonville Municipal Airport (K17J) | Decatur County Industrial Air Park (KBGE) | 2026-06-06 11:29 UTC | 2026-06-06 11:35 UTC | 5m |
| SPMOC | SPM | Pobiednik Wielki Airport (EPKP) | Pobiednik Wielki Airport (EPKP) | 2026-06-06 11:19 UTC | 2026-06-06 11:33 UTC | 13m |
| RYR4TR | Ryanair | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Gothenburg-Landvetter Airport (ESGG) | 2026-06-06 09:13 UTC | 2026-06-06 11:31 UTC | 2h 18m |
| PSMRT | PSM | Municipal Bom Futuro Airport (SILC) | Fazenda Boa Vista Airport (SWQM) | 2026-06-06 10:56 UTC | 2026-06-06 11:30 UTC | 33m |
| OKZUN01 | OKZ | Havlickuv Brod Airport (LKHB) | Havlickuv Brod Airport (LKHB) | 2026-06-06 10:53 UTC | 2026-06-06 11:28 UTC | 35m |
| SNJ37 | SNJ | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 2026-06-06 09:58 UTC | 2026-06-06 11:25 UTC | 1h 26m |
| WIF1328 | WIF | Bodø Airport (ENBO) | Bardufoss Airport (ENDU) | 2026-06-06 10:52 UTC | 2026-06-06 11:21 UTC | 29m |
| EIN91W | Aer Lingus | London Heathrow Airport (EGLL) | Ireland West Knock Airport (EIKN) | 2026-06-06 10:18 UTC | 2026-06-06 11:20 UTC | 1h 2m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-06-06 11:09 UTC | 2026-06-06 11:18 UTC | 9m |
| OKOOO | OKO | Zell Am See Airport (LOWZ) | Zell Am See Airport (LOWZ) | 2026-06-06 10:36 UTC | 2026-06-06 11:16 UTC | 39m |
| 4XDAN |  | Bar Yehuda Airfield (LLMZ) | Bar Yehuda Airfield (LLMZ) | 2026-06-06 11:03 UTC | 2026-06-06 11:13 UTC | 10m |
| AIQ3925 | AIQ | Don Mueang International Airport (VTBD) | Tak Airport (VTPT) | 2026-06-06 10:41 UTC | 2026-06-06 11:11 UTC | 29m |
| N400G |  | Savannah/Hilton Head International Airport (KSAV) | Washington Dulles International Airport (KIAD) | 2026-06-06 09:57 UTC | 2026-06-06 11:08 UTC | 1h 11m |
| THA136 | Thai Airways | Suvarnabhumi Airport (VTBS) | Kengtung Airport (VYKG) | 2026-06-06 10:16 UTC | 2026-06-06 11:08 UTC | 52m |
| RUK80AJ | RUK | London Stansted Airport (EGSS) | Ifrane Airport (GMFI) | 2026-06-06 08:25 UTC | 2026-06-06 11:05 UTC | 2h 40m |
| ANE55FV | ANE | Palma De Mallorca Airport (LEPA) | Ibiza Airport (LEIB) | 2026-06-06 10:44 UTC | 2026-06-06 11:05 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
