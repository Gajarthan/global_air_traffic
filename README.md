# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--28_22:51:01_UTC-green)

![Flight Map](images/flight_map.png)

## About

Real-time tracking of global air traffic using the [OpenSky Network](https://opensky-network.org/) API. This repository automatically fetches live aircraft positions worldwide and generates visualizations and statistics.

**Data Source:** OpenSky Network REST API (`/states/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches all aircraft transponder data globally
- Maps on-ground aircraft to nearest airports (28,000+ airport database)
- Identifies airlines from ICAO callsign prefixes
- Generates a live flight map and summary statistics

## Live Snapshot

**2026-03-28 22:51:01 UTC**

- **8,432** aircraft tracked
- **7,709** currently in the air
- **723** on the ground
- **86** countries
- **100** airports with traffic
- **50** airlines identified
- **140** flight routes (last 2h)
- **1h 15m** average flight duration

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Delta Air Lines | 481 |
| 2 | Southwest Airlines | 473 |
| 3 | United Airlines | 467 |
| 4 | American Airlines | 458 |
| 5 | Ryanair | 205 |
| 6 | SkyWest Airlines | 182 |
| 7 | Alaska Airlines | 131 |
| 8 | JetBlue | 121 |
| 9 | EJA | 112 |
| 10 | Air Canada | 90 |
| 11 | FFT | 89 |
| 12 | Republic Airways | 84 |
| 13 | ENY | 77 |
| 14 | WJA | 71 |
| 15 | easyJet | 68 |
| 16 | AAY | 61 |
| 17 | JIA | 58 |
| 18 | LXJ | 57 |
| 19 | All Nippon Airways | 55 |
| 20 | NKS | 55 |
| 21 | EDV | 52 |
| 22 | Japan Airlines | 48 |
| 23 | AZU | 38 |
| 24 | Aeromexico | 37 |
| 25 | Lufthansa | 37 |
| 26 | PDT | 36 |
| 27 | Scandinavian Airlines | 36 |
| 28 | LATAM Airlines | 35 |
| 29 | CXK | 35 |
| 30 | Qantas | 35 |

## Top Countries (by aircraft registration)

| # | Country | Aircraft |
|---:|---------|--------:|
| 1 | 🇺🇸 United States | 5544 |
| 2 | 🇨🇦 Canada | 376 |
| 3 | 🇦🇺 Australia | 235 |
| 4 | 🇬🇧 United Kingdom | 205 |
| 5 | 🇯🇵 Japan | 175 |
| 6 | 🇮🇪 Ireland | 163 |
| 7 | 🇲🇽 Mexico | 120 |
| 8 | 🇨🇳 China | 108 |
| 9 | 🇧🇷 Brazil | 100 |
| 10 | 🏳️ Malta | 96 |
| 11 | 🇹🇷 Turkey | 92 |
| 12 | 🏳️ Republic of Korea | 84 |
| 13 | 🇳🇿 New Zealand | 73 |
| 14 | 🇩🇪 Germany | 72 |
| 15 | 🇪🇸 Spain | 67 |
| 16 | 🇮🇳 India | 57 |
| 17 | 🇫🇷 France | 46 |
| 18 | 🇦🇪 United Arab Emirates | 46 |
| 19 | 🇨🇱 Chile | 41 |
| 20 | 🇸🇪 Sweden | 35 |
| 21 | 🇵🇱 Poland | 35 |
| 22 | 🇲🇾 Malaysia | 35 |
| 23 | 🏳️ Kingdom of the Netherlands | 34 |
| 24 | 🇹🇼 Taiwan | 34 |
| 25 | 🇵🇭 Philippines | 32 |
| 26 | 🇦🇹 Austria | 30 |
| 27 | 🇸🇬 Singapore | 27 |
| 28 | 🇵🇹 Portugal | 27 |
| 29 | 🇪🇬 Egypt | 25 |
| 30 | 🇹🇭 Thailand | 24 |

## Busiest Airports (aircraft on ground)

| # | Airport | City | Country | Aircraft |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport | Dallas-Fort Worth | US | 29 |
| 2 | Hartsfield/Jackson Atlanta International Airport | Atlanta | US | 29 |
| 3 | Phoenix Sky Harbor International Airport | Phoenix | US | 26 |
| 4 | Sydney Kingsford Smith International Airport | Sydney | AU | 24 |
| 5 | Toronto Pearson International Airport | Mississauga | CA | 23 |
| 6 | Tokyo International Airport | Tokyo | JP | 19 |
| 7 | Orlando International Airport | Orlando | US | 18 |
| 8 | Harry Reid International Airport | Las Vegas | US | 17 |
| 9 | John F Kennedy International Airport | New York | US | 16 |
| 10 | Southwest Florida International Airport | Fort Myers | US | 16 |
| 11 | Calgary International Airport | Calgary | CA | 16 |
| 12 | Newark Liberty International Airport | Newark | US | 16 |
| 13 | Laguardia Airport | New York | US | 16 |
| 14 | Cancun International Airport | Cancun | MX | 15 |
| 15 | Chicago O'Hare International Airport | Chicago | US | 14 |
| 16 | Melbourne International Airport | Melbourne | AU | 13 |
| 17 | General Edward Lawrence Logan International Airport | Boston | US | 12 |
| 18 | San Francisco International Airport | San Francisco | US | 12 |
| 19 | Los Angeles International Airport | Los Angeles | US | 12 |
| 20 | Vancouver International Airport | Richmond | CA | 12 |
| 21 | Tampa International Airport | Tampa | US | 9 |
| 22 | Washington Dulles International Airport | Washington | US | 9 |
| 23 | Chhatrapati Shivaji International Airport | Mumbai | IN | 8 |
| 24 | Denver International Airport | Denver | US | 8 |
| 25 | Norman Y Mineta San Jose International Airport | San Jose | US | 8 |
| 26 | Chek Lap Kok International Airport | Hong Kong | HK | 8 |
| 27 | Salt Lake City International Airport | Salt Lake City | US | 7 |
| 28 | Ronald Reagan Washington Ntl Airport | Washington | US | 7 |
| 29 | Teterboro Airport | Teterboro | US | 6 |
| 30 | Austin-Bergstrom International Airport | Austin | US | 6 |
| 31 | Dubuque Regional Airport | Dubuque | US | 6 |
| 32 | Montréal-Pierre Elliott Trudeau International Airport | Dorval | CA | 5 |
| 33 | Indira Gandhi International Airport | New Delhi | IN | 5 |
| 34 | Van Nuys Airport | Van Nuys | US | 5 |
| 35 | Riverside Airport | Riverside | US | 5 |
| 36 | St Louis Lambert International Airport | St Louis | US | 5 |
| 37 | Chicago Midway International Airport | Chicago | US | 5 |
| 38 | North Las Vegas Airport | Las Vegas | US | 5 |
| 39 | Albuquerque International Sunport Airport | Albuquerque | US | 5 |
| 40 | San Diego International Airport | San Diego | US | 5 |

## Top Routes (last 2 hours)

| # | From | To | Flights | Avg Duration |
|---:|------|-----|--------:|------------:|
| 1 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 2 | 14m |
| 2 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 2 | 30m |
| 3 | Denver International Airport (KDEN) | Morrilton Airport (07AR) | 2 | 1h 22m |
| 4 | Vancouver International Airport (CYVR) | Kaslo Airport (CBR2) | 2 | 46m |
| 5 | Rafael Nunez International Airport (SKCG) | Alfonso Lopez Pumarejo Airport (SKVP) | 1 | 19m |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 1 | 21m |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 1 | 32m |
| 8 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 1 | 29m |
| 9 | Licenciado Benito Juarez International Airport (MMMX) | Atizapan De Zaragoza Airport (MMJC) | 1 | 13m |
| 10 | Barcelona International Airport (LEBL) | Federico Garcia Lorca Airport (LEGR) | 1 | 1h 14m |
| 11 | Alicante International Airport (LEAL) | Mostaganem Airport (DA14) | 1 | 24m |
| 12 | Václav Havel Airport (LKPR) | Niksic Airport (LYNK) | 1 | 1h 9m |
| 13 | John Paul II International Airport Kraków-Balice Airport (EPKK) | Cemovsko Polje Airport (LYPO) | 1 | 1h 4m |
| 14 | London Stansted Airport (EGSS) | Frankfurt-Hahn Airport (EDFH) | 1 | 51m |
| 15 | Alicante International Airport (LEAL) | Malpensa International Airport (LIMC) | 1 | 1h 39m |
| 16 | Brussels South Charleroi Airport (EBCI) | Tivat Airport (LYTV) | 1 | 1h 42m |
| 17 | Riga International Airport (EVRA) | Zurich Airport (LSZH) | 1 | 2h 18m |
| 18 | VGZR (VGZR) | Macau International Airport (VMMC) | 1 | 2h 40m |
| 19 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 1 | 11h 34m |
| 20 | Toowoomba Wellcamp Airport (YBWW) | Ballina Byron Gateway Airport (YBNA) | 1 | 1h 25m |
| 21 | London Gatwick Airport (EGKK) | Fujairah International Airport (OMFJ) | 1 | 6h 39m |
| 22 | Charles de Gaulle International Airport (LFPG) | Fujairah International Airport (OMFJ) | 1 | 6h 25m |
| 23 | Shaibah Airport (OESB) | HE42 (HE42) | 1 | 3h 52m |
| 24 | Midland International Air And Space Port Airport (KMAF) | Andrews County Airport (KE11) | 1 | 12m |
| 25 | Provo Municipal Airport (KPVU) | K36U (K36U) | 1 | 11m |
| 26 | Miami International Airport (KMIA) | Laguardia Airport (KLGA) | 1 | 2h 28m |
| 27 | Addison Airport (KADS) | Manassas Regional/Harry P Davis Field (KHEF) | 1 | 2h 14m |
| 28 | Modesto City-County-Harry Sham Field (KMOD) | Lake Tahoe Airport (KTVL) | 1 | 34m |
| 29 | San Francisco International Airport (KSFO) | 3CO0 (3CO0) | 1 | 1h 40m |
| 30 | Julian Hinds Pump Plant Airstrip (73CL) | Henderson Executive Airport (KHND) | 1 | 27m |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N7718A |  | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 2026-03-28 21:55 UTC | 2026-03-28 22:33 UTC | 38m |
| EFI | EFI | Toowoomba Wellcamp Airport (YBWW) | Ballina Byron Gateway Airport (YBNA) | 2026-03-28 20:58 UTC | 2026-03-28 22:23 UTC | 1h 25m |
| N5767G |  | Santa Monica Municipal Airport (KSMO) | Santa Monica Municipal Airport (KSMO) | 2026-03-28 21:15 UTC | 2026-03-28 22:16 UTC | 1h 0m |
| N9452B |  | New Jerusalem Airport (K1Q4) | CA54 (CA54) | 2026-03-28 16:51 UTC | 2026-03-28 22:15 UTC | 5h 23m |
| AUB162 | AUB | Auburn University Regional Airport (KAUO) | Auburn University Regional Airport (KAUO) | 2026-03-28 21:49 UTC | 2026-03-28 22:14 UTC | 25m |
| N929KT |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-03-28 21:40 UTC | 2026-03-28 22:14 UTC | 33m |
| N121AP |  | Addison Airport (KADS) | Manassas Regional/Harry P Davis Field (KHEF) | 2026-03-28 19:58 UTC | 2026-03-28 22:13 UTC | 2h 14m |
| ZKTTL | ZKT | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 2026-03-28 21:51 UTC | 2026-03-28 22:09 UTC | 17m |
| CPA662 | Cathay Pacific | VGZR (VGZR) | Macau International Airport (VMMC) | 2026-03-28 19:27 UTC | 2026-03-28 22:08 UTC | 2h 40m |
| LT617 |  | Ensenada Airport (MMES) | Imperial Beach Nolf (Ream Field) Airport (KNRS) | 2026-03-28 20:19 UTC | 2026-03-28 22:07 UTC | 1h 48m |
| SCU13 | SCU | Double W Airport (3OK7) | Barcus Field (95OK) | 2026-03-28 21:45 UTC | 2026-03-28 22:06 UTC | 20m |
| CPA698 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-03-28 10:29 UTC | 2026-03-28 22:03 UTC | 11h 34m |
| N724D |  | Aero Country Airport (KT31) | TX68 (TX68) | 2026-03-28 21:31 UTC | 2026-03-28 22:01 UTC | 29m |
| EJA836 | EJA | El Paso International Airport (KELP) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-03-28 20:52 UTC | 2026-03-28 21:59 UTC | 1h 6m |
| N65641 |  | Blue Grass Airport (KLEX) | Georgetown-Scott County Regional Airport (K27K) | 2026-03-28 21:45 UTC | 2026-03-28 21:58 UTC | 13m |
| LXJ386 | LXJ | Butler Municipal Airport (K6A1) | Witham Field (KSUA) | 2026-03-28 20:52 UTC | 2026-03-28 21:57 UTC | 1h 5m |
| N350BV |  | Meadows Field (KBFL) | Van Nuys Airport (KVNY) | 2026-03-28 21:37 UTC | 2026-03-28 21:56 UTC | 19m |
| N541LC |  | Daniel K Inouye International Airport (PHNL) | Lanai Airport (PHNY) | 2026-03-28 20:59 UTC | 2026-03-28 21:53 UTC | 54m |
| CWA922 | CWA | Calgary International Airport (CYYC) | Milk River Airport (CEW5) | 2026-03-28 21:26 UTC | 2026-03-28 21:53 UTC | 26m |
| EJA890 | EJA | Los Angeles International Airport (KLAX) | Jerome County Airport (KJER) | 2026-03-28 20:32 UTC | 2026-03-28 21:52 UTC | 1h 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
