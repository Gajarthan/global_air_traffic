# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_23:26:43_UTC-green)

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

**Latest saved flight:** 2026-05-17 23:26:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-17 23:26:43 UTC

- **87,080** saved flights
- **31,174** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **87,080** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,078,101.0 tonnes** estimated CO2 emissions
- **62,498,608 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3730 |
| 2 | SkyWest Airlines | 3224 |
| 3 | IndiGo | 1866 |
| 4 | EJA | 1647 |
| 5 | American Airlines | 1337 |
| 6 | Southwest Airlines | 1268 |
| 7 | Lufthansa | 1098 |
| 8 | ENY | 1081 |
| 9 | Delta Air Lines | 957 |
| 10 | Vueling | 828 |
| 11 | LATAM Airlines | 788 |
| 12 | AXM | 782 |
| 13 | WIF | 742 |
| 14 | AZU | 686 |
| 15 | Swiss International | 674 |
| 16 | All Nippon Airways | 667 |
| 17 | LXJ | 642 |
| 18 | QLK | 626 |
| 19 | Alaska Airlines | 618 |
| 20 | easyJet | 575 |
| 21 | EJU | 560 |
| 22 | Cathay Pacific | 555 |
| 23 | AEE | 542 |
| 24 | VIV | 523 |
| 25 | Air France | 510 |
| 26 | Japan Airlines | 479 |
| 27 | CXK | 459 |
| 28 | AXB | 455 |
| 29 | MXY | 440 |
| 30 | AIQ | 427 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 71368 |
| 2 | 🇪🇸 ES | 6170 |
| 3 | 🇮🇳 IN | 5838 |
| 4 | 🇦🇺 AU | 5486 |
| 5 | 🇩🇪 DE | 4850 |
| 6 | 🇮🇹 IT | 4820 |
| 7 | 🇧🇷 BR | 4788 |
| 8 | 🇨🇦 CA | 4330 |
| 9 | 🇯🇵 JP | 4323 |
| 10 | 🇬🇧 GB | 3721 |
| 11 | 🇫🇷 FR | 3480 |
| 12 | 🇨🇴 CO | 2932 |
| 13 | 🇲🇽 MX | 2705 |
| 14 | 🇬🇷 GR | 2527 |
| 15 | 🇳🇴 NO | 2401 |
| 16 | 🇨🇭 CH | 2311 |
| 17 | 🇲🇾 MY | 1964 |
| 18 | 🇿🇦 ZA | 1621 |
| 19 | 🇹🇷 TR | 1577 |
| 20 | 🇳🇿 NZ | 1519 |
| 21 | 🇹🇭 TH | 1503 |
| 22 | 🇵🇱 PL | 1445 |
| 23 | 🇰🇷 KR | 1360 |
| 24 | 🇵🇭 PH | 1354 |
| 25 | 🇬🇹 GT | 1313 |
| 26 | 🇲🇴 MO | 1014 |
| 27 | 🇲🇦 MA | 1011 |
| 28 | 🇲🇪 ME | 904 |
| 29 | 🇳🇱 NL | 890 |
| 30 | 🇭🇷 HR | 783 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1910 |
| 2 | Denver International Airport |  | US | 1457 |
| 3 | Tokyo International Airport |  | JP | 1444 |
| 4 | Indira Gandhi International Airport |  | IN | 1254 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1203 |
| 6 | Frankfurt am Main International Airport |  | DE | 1110 |
| 7 | Harry Reid International Airport |  | US | 1109 |
| 8 | Zurich Airport |  | CH | 1039 |
| 9 | Macau International Airport |  | MO | 1014 |
| 10 | La Aurora Airport |  | GT | 998 |
| 11 | Guaymaral Airport |  | CO | 990 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 965 |
| 13 | El Dorado International Airport |  | CO | 941 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 878 |
| 15 | Chicago O'Hare International Airport |  | US | 844 |
| 16 | Madrid Barajas International Airport |  | ES | 793 |
| 17 | Kuala Lumpur International Airport |  | MY | 780 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 749 |
| 19 | Capua Airport |  | IT | 731 |
| 20 | Salt Lake City International Airport |  | US | 728 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 717 |
| 22 | Malpensa International Airport |  | IT | 714 |
| 23 | Bengaluru International Airport |  | IN | 706 |
| 24 | Charles de Gaulle International Airport |  | FR | 679 |
| 25 | Charlotte/Douglas International Airport |  | US | 677 |
| 26 | Congonhas Airport |  | BR | 669 |
| 27 | Daniel K Inouye International Airport |  | US | 639 |
| 28 | Tenerife Norte Airport |  | ES | 639 |
| 29 | Ninoy Aquino International Airport |  | PH | 620 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 596 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 595 |
| 32 | Barcelona International Airport |  | ES | 585 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 580 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 558 |
| 35 | Vitoria/Foronda Airport |  | ES | 555 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 550 |
| 37 | Don Mueang International Airport |  | TH | 545 |
| 38 | Amsterdam Airport Schiphol |  | NL | 544 |
| 39 | Calgary International Airport |  | CA | 512 |
| 40 | O. R. Tambo International Airport |  | ZA | 510 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 408 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 324 | 21m | 244 km | 1,364.3 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 276 | 1h 8m | 706 km | 3,360.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 243 | 24m | 225 km | 942.7 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 230 | 1h 26m | 910 km | 3,609.2 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 227 | 28m | 304 km | 1,190.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 224 | 14m | 114 km | 439.3 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 222 | 9m | - | - |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 200 | 1h 10m | 770 km | 2,656.8 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 193 | 19m | 165 km | 549.0 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 182 | 26m | 275 km | 862.4 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 146 | 21m | 99 km | 250.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 136 | 31m | 369 km | 865.7 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 132 | 27m | 152 km | 345.0 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 126 | 27m | 215 km | 466.7 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 126 | 20m | 147 km | 318.9 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 124 | 14m | 154 km | 328.6 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 123 | 23m | 55 km | 116.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 121 | 20m | 250 km | 522.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 111 | 1h 42m | 1,423 km | 2,724.1 t |
| 26 | Bodø Airport (ENBO) | ENEN (ENEN) | 111 | 13m | - | - |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 111 | 18m | 144 km | 276.1 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 108 | 12m | - | - |
| 29 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 106 | 1h 52m | 1,304 km | 2,384.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-05-17 23:14 UTC | 2026-05-17 23:26 UTC | 12m |
| CFR93 | CFR | Bodad Airport (CA11) | Redding Regional Airport (KRDD) | 2026-05-17 23:11 UTC | 2026-05-17 23:24 UTC | 13m |
| SRP4 | SRP | Koblenz-Winningen Airport (EDRK) | Elz Airport (EDFY) | 2026-05-17 22:10 UTC | 2026-05-17 23:18 UTC | 1h 8m |
| HKC9458 | HKC | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-05-17 18:51 UTC | 2026-05-17 23:13 UTC | 4h 22m |
| MNB6560 | MNB | Istanbul Hezarfen Airfield (LTBW) | Macau International Airport (VMMC) | 2026-05-17 11:12 UTC | 2026-05-17 23:05 UTC | 11h 53m |
| FRLD33 | FRL | Mesa Gateway Airport (KIWA) | San Carlos Apache Airport (KP13) | 2026-05-17 22:50 UTC | 2026-05-17 23:04 UTC | 14m |
| TKR104 | TKR | 6CO3 (6CO3) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-05-17 22:32 UTC | 2026-05-17 22:58 UTC | 25m |
| TKR102 | TKR | Melon Field (1CO5) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-05-17 22:43 UTC | 2026-05-17 22:58 UTC | 14m |
| FFL1414 | FFL | Eppley Airfield (KOMA) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-17 22:08 UTC | 2026-05-17 22:57 UTC | 48m |
| TKR101 | TKR | Mc Clellan Airfield (KMCC) | Bodad Airport (CA11) | 2026-05-17 22:15 UTC | 2026-05-17 22:57 UTC | 42m |
| N559BG |  | La Aurora Airport (MGGT) | Chumbagua Airport (MHGA) | 2026-05-17 22:25 UTC | 2026-05-17 22:57 UTC | 31m |
| ACW2730 | ACW | Teterboro Airport (KTEB) | General Mariano Escobedo International Airport (MMMY) | 2026-05-17 18:54 UTC | 2026-05-17 22:56 UTC | 4h 2m |
| XSR487 | XSR | Harry Reid International Airport (KLAS) | Northern Colorado Regional Airport (KFNL) | 2026-05-17 21:34 UTC | 2026-05-17 22:55 UTC | 1h 21m |
| CPA382 | Cathay Pacific | Zurich Airport (LSZH) | Macau International Airport (VMMC) | 2026-05-17 12:10 UTC | 2026-05-17 22:53 UTC | 10h 42m |
| N7426 |  | Eugene F Kranz Toledo Express Airport (KTOL) | Savannah/Hilton Head International Airport (KSAV) | 2026-05-17 21:27 UTC | 2026-05-17 22:52 UTC | 1h 24m |
| CPA318 | Cathay Pacific | Barcelona International Airport (LEBL) | Macau International Airport (VMMC) | 2026-05-17 11:37 UTC | 2026-05-17 22:51 UTC | 11h 13m |
| N63FS |  | Clark Regional Airport (KJVY) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-05-17 21:59 UTC | 2026-05-17 22:50 UTC | 50m |
| N711FP |  | Easterwood Field (KCLL) | Addington Field (4TX8) | 2026-05-17 22:11 UTC | 2026-05-17 22:49 UTC | 38m |
| LR453 |  | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-05-17 22:13 UTC | 2026-05-17 22:47 UTC | 34m |
| N928NG |  | Iowa City Municipal Airport (KIOW) | Johnson County Executive Airport (KOJC) | 2026-05-17 21:35 UTC | 2026-05-17 22:46 UTC | 1h 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
